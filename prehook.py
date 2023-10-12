import os
from database_handler import return_query,execute_query, create_connection, close_connection,return_data_as_df
from pandas_data_handler import return_create_statement_from_df,return_insert_into_sql_statement_from_df
from misc_handler import execute_sql_folder,create_insert_sql,enum_to_lists
from lookups import ErrorHandling, InputTypes,DestinationDatabase,ETLStep,studies
from logging_handler import show_error_message
import pandas as pd

def execute_prehook(sql_command_directory_path = './SQL_Commands'):
    try:
        
        db_session = create_connection()
        execute_sql_folder(db_session, sql_command_directory_path, ETLStep.PRE_HOOK, DestinationDatabase.SCHEMA_NAME)
        df_src_titles,df_src_content=enum_to_lists(studies)
        create_insert_sql(db_session, DestinationDatabase.DATABASE_NAME, df_src_content, df_src_titles,etl_step=ETLStep.PRE_HOOK)
        close_connection(db_session)
        


    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.PREHOOK_SQL_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Important Step Failed")
