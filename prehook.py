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
    logging.info(" Executing Prehook :")
    try:
        logging.info(" Creating Database Connection :")
        db_session = create_connection()
        logging.info(" Step 2 Creating Schema :")
        execute_sql_folder(
            db_session,
            sql_command_directory_path,
            ETLStep.PRE_HOOK,
            DestinationDatabase.SCHEMA_NAME,
        )
        logging.info(" Step 3 Executing ML Classification and Prediction")
        execute_ml_classification_prediction(
            "https://heartdisease246.s3.amazonaws.com/heart_statlog_cleveland_hungary_final+(11).csv",
            "ML Process and Output",
        )
        logging.info(" Step 4 Creating Staging Tables")

        create_insert_sql(
            db_session,
            DestinationDatabase.DATABASE_NAME,
            links,
            etl_step=ETLStep.PRE_HOOK,
            input_type=InputTypes.CSV,
        )
        logging.info(" Step 5 Closing Connection")

        close_connection(db_session)

        return
    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.PREHOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
