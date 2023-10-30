import os
from lookups import ErrorHandling, ETLStep, InputTypes, links
from database_handler import (
    execute_query,
    return_data_as_df,
)
from pandas_data_handler import (
    download_csv_to_dataframe,
    return_create_statement_from_df,
    return_insert_into_sql_statement_from_df,
)
from logging_handler import show_error_message
import pandas as pd
import os
import re
from lookups import *


def return_lookup_items_as_dict(lookup_item):
    enum_dict = {
        str(item.name).lower(): item.value.replace(item.name.lower() + "_", "")
        for item in lookup_item
    }
    return enum_dict


def enum_to_lists(enum_class):
    names = [item.name.lower() for item in enum_class]
    links = [str(item.value) for item in enum_class]
    return names, links


def execute_sql_folder(db_session, sql_command_directory_path, etl_step, target_schema):
    sql_files = [
        sqlfile
        for sqlfile in os.listdir(sql_command_directory_path)
        if sqlfile.endswith(".sql")
    ]
    sorted_sql_files = sorted(
        sql_files, key=lambda x: int(re.search(r"V(\d+)\s*__\s*(\w+)", x).group(1))
    )
    counter = 0
    for sql_file in sorted_sql_files:
        counter += 1
        match = re.search(r"V(\d+)\s*__\s*(\w+)", sql_file)
        if match:
            version, step = match.groups()
            step = step.split("_")[0]
            if step == etl_step.value:
                with open(
                    os.path.join(sql_command_directory_path, sql_file), "r"
                ) as file:
                    sql_query = file.read()
                    sql_query = sql_query.replace("target_schema", target_schema.value)

                    return_val = execute_query(db_session=db_session, query=sql_query)
                    if not return_val == ErrorHandling.NO_ERROR:
                        raise Exception(
                            f"Error executing SQL File on = " + str(sql_file)
                        )


def create_insert_sql(
    db_session, source_name, links, etl_step, input_type=None, etl_date=None
):
    try:
        source_name = source_name.value
        lookups_items = return_lookup_items_as_dict(links)

        for table_name, source_df in lookups_items.items():
            dataframe_source = download_csv_to_dataframe(source_df)
            dst_table = f"stg_{source_name}_{table_name}"
            staging_df = pd.DataFrame()
            if etl_step == ETLStep.PRE_HOOK:
                create_stmt = return_create_statement_from_df(
                    dataframe_source, "dw_reporting", dst_table
                )

                execute_query(db_session=db_session, query=create_stmt)

            elif etl_step == ETLStep.HOOK:
                dataframe_source["date_added"] = pd.to_datetime(
                    dataframe_source["date_added"]
                )
                etl_date = pd.to_datetime(etl_date)
                if dataframe_source["date_added"].min() > etl_date:
                    staging_df = dataframe_source
                else:
                    staging_df = dataframe_source[
                        dataframe_source["date_added"] > etl_date
                    ]
                if len(staging_df) > 0:
                    insert_stmt = return_insert_into_sql_statement_from_df(
                        staging_df, "dw_reporting", dst_table
                    )
                    execute_query(db_session=db_session, query=insert_stmt)

    except Exception as error:
        suffix = str(error)
        error_prefix = ErrorHandling.CREATE_INSERT_STAGING_TABLES_ERROR
        show_error_message(error_prefix.value, suffix)
        raise Exception("Error creating/insert into staging tables")
