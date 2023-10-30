from database_handler import (
    execute_query,
    create_connection,
    close_connection,
    return_data_as_df,
)

from lookups import ErrorHandling, InputTypes, ETLStep, DestinationDatabase
from datetime import datetime
from misc_handler import  execute_sql_folder, create_insert_sql
from logging_handler import show_error_message
from lookups import *
import logging


def create_etl_checkpoint(db_session):
    try:
        query = f"""
            CREATE TABLE IF NOT EXISTS dw_reporting.etl_checkpoint
            (
                etl_last_run_date TIMESTAMP
            )
            """
        execute_query(db_session, query)
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.ETL_CHECKPOINT_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")


def insert_or_update_etl_checkpoint(db_session, does_etl_time_exists, etl_date=None):
    if does_etl_time_exists:
        status, status_message = ErrorHandling.ETL_UPDATE_CHECKPOINT_ERROR, "updating"
        insert_update_stmnt = (
            f"UPDATE dw_reporting.etl_checkpoint SET etl_last_run_date = '{etl_date}'"
        )

    else:
        status, status_message = ErrorHandling.ETL_INSERT_CHECKPOINT_ERROR, "inserting"
        insert_update_stmnt = f"INSERT INTO dw_reporting.etl_checkpoint (etl_last_run_date) VALUES ('{etl_date}')"

    try:
        execute_query(db_session, insert_update_stmnt)
    except Exception as e:
        suffix = str(e)
        error_prefix = status
        show_error_message(error_prefix.value, suffix)
        raise Exception(f"Error while {status_message} ETL checkpoint")


def return_etl_last_updated_date(db_session, target_schema, table):
    does_etl_time_exists = False
    query = f"SELECT etl_last_run_date FROM {target_schema}.{table} ORDER BY etl_last_run_date DESC LIMIT 1"

    try:
        etl_df = return_data_as_df(
            file_executor=query, input_type=InputTypes.SQL, db_session=db_session
        )
        if len(etl_df) == 0:
            return_date = "12-9-1945"
        else:
            return_date = etl_df["etl_last_run_date"].iloc[0]
            does_etl_time_exists = True
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.RETURN_ETL_LAST_UPDATE_ERROR
        show_error_message(error_prefix.value, suffix)
    finally:
        return return_date, does_etl_time_exists


def execute_hook():
    try:
        db_session = create_connection()
        create_etl_checkpoint(db_session)
        etl_date, does_etl_time_exists = return_etl_last_updated_date(
            db_session,
            DestinationDatabase.SCHEMA_NAME.value,
            ETL_CHECK_POINT_TABLE.ETL_CHECKPOINT.value,
        )

        create_insert_sql(
            db_session,
            DestinationDatabase.DATABASE_NAME,
            links,
            ETLStep.HOOK,
            InputTypes.CSV,
            etl_date,
        )
        logging.info(" Successfully inserted new data into the staging tables   ")
        execute_sql_folder(
            db_session, "SQL_COMMANDS", ETLStep.HOOK, DestinationDatabase.SCHEMA_NAME
        )
        logging.info("Hook execute folder was executed ")
        logging.info("Data were successfully inserted to relational database !")
        # last step
        insert_or_update_etl_checkpoint(
            db_session, does_etl_time_exists, datetime.now()
        )
        logging.info(" successfully Updated check point ")
        close_connection(db_session)

    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.HOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
