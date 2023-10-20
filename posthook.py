from database_handler import execute_query, create_connection
import misc_handler
from lookups import DestinationDatabase
from misc_handler import enum_to_lists
from lookups import studies
from lookups import ETLStep
from lookups import ErrorHandling
from logging_handler import show_error_message

def truncate_staging_tables(source_name,schema_name, table_list, db_session):
    for table in table_list:
        truncate_query = f"""
        DO $$ 
        DECLARE
            index_to_drop TEXT;
        BEGIN
            IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = '{schema_name.value}' AND table_name = '{table}') THEN
                TRUNCATE TABLE {schema_name.value}.{table};
                RAISE NOTICE 'Table truncated successfully.';
                SELECT 
                    CONCAT('{schema_name.value}.',indexname) 
                INTO index_to_drop
                FROM pg_indexes 
                WHERE tablename = '{table}'
                AND SUBSTRING(indexname FROM 1 FOR 4) = 'idx_';
                IF index_to_drop IS NOT NULL THEN
                    EXECUTE 'DROP INDEX ' || index_to_drop;
                ELSE 
                    RAISE NOTICE 'Index not found';
                END IF;
            ELSE
                RAISE NOTICE 'Table does not exist.';
            END IF;
        END $$;
            """
        execute_query(db_session, truncate_query)



def execute_posthook():
    db_session = create_connection()
    df_title,source=enum_to_lists(studies)
    tables = misc_handler.create_insert_sql(db_session,DestinationDatabase.DATABASE_NAME,df_title,source, ETLStep.POSTHOOK)
    truncate_staging_tables(DestinationDatabase.DATABASE_NAME,DestinationDatabase.SCHEMA_NAME, tables, db_session)
