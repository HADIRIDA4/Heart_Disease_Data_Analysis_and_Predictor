import os
from database_handler import (
    create_connection,
    close_connection,
)
from ml_handler import execute_ml_classification_prediction
from misc_handler import execute_sql_folder, create_insert_sql
from logging_handler import show_error_message
from lookups import *
import logging


def execute_prehook(sql_command_directory_path="./SQL_Commands"):
    try:
        db_session = create_connection()

        execute_sql_folder(
            db_session,
            sql_command_directory_path,
            ETLStep.PRE_HOOK,
            DestinationDatabase.SCHEMA_NAME,
        )
        logging.info(
            " PREHOOK SQL FOLDER WAS Successfully executed : Schema was created ! "
        )

        execute_ml_classification_prediction(
            "https://storage.googleapis.com/csv-links/heart_statlog_cleveland_hungary_final.csv",
            "ML_output",
        )
        logging.info(" Prediction and classification were executed! ")

        create_insert_sql(
            db_session,
            DestinationDatabase.DATABASE_NAME,
            links,
            etl_step=ETLStep.PRE_HOOK,
            input_type=InputTypes.CSV,
        )
        logging.info(
            " PREHOOK SQL FOLDER WAS Successfully executed : SQL Staging tables were created ! "
        )
        close_connection(db_session)
        return
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.PREHOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
