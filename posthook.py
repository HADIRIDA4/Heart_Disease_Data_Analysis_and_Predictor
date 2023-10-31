from misc_handler import *
from lookups import *
from database_handler import *
import logging


def truncate_staging_tables(db_name, schema_name, links):
    db_session = create_connection()
    # source_name = source_name.value
    for table in return_lookup_items_as_dict(links).keys():
        dst_table = f"{schema_name}.stg_{db_name}_{table}"
        truncate_query = f"""
        TRUNCATE TABLE  {dst_table}"""
        execute_query(db_session, truncate_query)


def execute_posthook():
    logging.info(" Posthook Phase Started ")

    truncate_staging_tables(
        DestinationDatabase.DATABASE_NAME.value,
        DestinationDatabase.SCHEMA_NAME.value,
        links,
    )
    logging.info("  Truncated Staging Tables ")
