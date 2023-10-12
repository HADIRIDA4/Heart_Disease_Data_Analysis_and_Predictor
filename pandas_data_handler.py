import pandas as pd
import os
import requests
import io
from io import BytesIO
from io import StringIO
from lookups import InputTypes, ErrorHandling
from logging_handler import show_error_message
from database_handler import return_data_as_df


def return_create_statement_from_df(dataframe, schema_name, table_name):
    type_mapping = {
        'int64': 'BIGINT',
        'float64': 'FLOAT',
        'datetime64[ns]': 'TIMESTAMP',
        'bool': 'BOOLEAN',
        'object': 'TEXT'
    }
    fields = []
    create_table_statement = None

    try:
        if dataframe.index.name:
            sql_type = type_mapping.get(str(dataframe.index.dtype), 'TEXT')
            modified_index_col = dataframe.index.name.replace(" ", "_").replace("-", "_")
            fields.append(f"{modified_index_col} {sql_type} PRIMARY KEY")


        for column, dtype in dataframe.dtypes.items():
            modified_column = column.replace(" ", "_").replace("-", "_")
            sql_type = type_mapping.get(str(dtype), 'TEXT')
            fields.append(f"{modified_column} {sql_type}")

        create_table_statement = f"CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (\n"
        create_table_statement += ",\n".join(fields)
        create_table_statement += "\n);"

    except Exception as error:
        error_prefix = ErrorHandling.CREATE_TABLE_ERROR.value
        suffix = str(error)
        show_error_message(error_prefix, suffix)
    finally:
        return create_table_statement


def return_insert_into_sql_statement_from_df(dataframe, schema_name, table_name):

    insert_statement = None
    try:

        if dataframe.index.name:
            dataframe.reset_index(inplace=True)

        columns = [column.replace(" ", "_").replace("-", "_")
                   for column in dataframe.columns]
        columns = ', '.join(columns)
        values_list = []
        for _, row in dataframe.iterrows():
            value_strs = []
            for val in row.values:

                if isinstance(val, list):
                    values = ",".join(val)
                    value_strs.append(f"'[{values}]'")
                elif pd.isna(val):
                    value_strs.append("NULL")
                elif isinstance(val, str):
                    # Escape single quotes in the string
                    val_escaped = val.replace("'", "''")
                    value_strs.append(f"'{val_escaped}'")
                elif isinstance(val, pd.Timestamp):
                    value_strs.append(f"'{val}'")
                else:
                    value_strs.append(str(val))
            values = ', '.join(value_strs)

            values_list.append(f"({values})")

        values_list = ',\n'.join(values_list)

        insert_statement = f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES\n {values_list};"

    except Exception as error:
        error_prefix = ErrorHandling.INSERT_INTO_TABLE_ERROR.value
        suffix = str(error)
        show_error_message(error_prefix, suffix)
    finally:

        return insert_statement


