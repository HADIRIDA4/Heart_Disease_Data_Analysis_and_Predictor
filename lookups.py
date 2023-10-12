from enum import Enum


class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    CREATE_TABLE_ERROR = "Error creating new table"
    INSERT_INTO_TABLE_ERROR = "Error inserting into table"
    STAGING_DATA_ERROR = "Error staging recent data"
    CREATE_INSERT_STAGING_TABLES_ERROR = "Error creating/inserting into staging tables"
    ETL_CHECKPOINT_ERROR = "Error creating ETL checkpoint"
    ETL_INSERT_CHECKPOINT_ERROR = "Error inserting ETL checkpoint"
    ETL_UPDATE_CHECKPOINT_ERROR = "Error updating ETL checkpoint"
    FUNCTION_NA = "Function not available"
    NO_ERROR = "No Errors"
    PREHOOK_SQL_ERROR = "Prehook: SQL Error"
    HOOK_SQL_ERROR = "Hook: SQL Error"
    DATE_CONVERSION_ERROR = "Warning: column is not a date format"
    RETURN_ETL_LAST_UPDATE_ERROR = "Error returning ETL last update"
    

class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"
    HTTP = "Http"

class prediction(Enum):
    BRAIN_STROKE_DS=r"csv\Brain_stroke_prediction_dataset.csv"
    CARDIO_PREDICTION=r"csv\cardio_prediction.csv"
    FRAMINGHAM_PREDICTION=r"csv\Framingham_prediction.csv"
   

class studies(Enum):
    FRAMINGHAM_STUDY=r"csv\Framingham_Study.csv"
    SWITZERLAND=r"csv\Switzerland.csv" 
    CLEVELAND=r"csv/CVD_cleaned.csv"
    DISEASE=r"csv\Disease.csv"
    INCIDENCE_GLOBAL=r"csv\incidence_global.csv"
    INCIDENCE_LEBANON=r"csv\incidence_lebanon.csv"
    MORATLITY_LEBANON=r"csv\mortality_lebanon.csv"
    MORATLITY_GLOBAL=r"csv\moratlity_global.csv"
    PREVALENCE_GLOBAL=r"csv/prevalence_global.csv"
    PREVALENCE_LEBANON=r"csv\prevalence_lebanon.csv"




class DestinationDatabase(Enum):
    SCHEMA_NAME = "dw_reporting"
    DATABASE_NAME = "heart_db"



class fields:
    pass



class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"