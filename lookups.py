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


class links(Enum):
    DISEASE_CATEGORY = r"temp_csv\disease_category (1) (1).csv"
    DISEASE = r"temp_csv\disease (2) (1).csv"
    EPIDEMIOLOGY = r"temp_csv/epidemiological data (2) (1).csv"
    FRAMINGHAM_STUDY = r"temp_csv/Framingham_Study (2) (2).csv"
    LOCATION = r"temp_csv/location (1) (1).csv"
    MEASURES = r"temp_csv/measures (2) (1).csv"
    SWITZERLAND_STUDY = r"temp_csv\Switzerland (1) (1).csv"

    CVD_CLEANED = r"temp_csv/cleveland (2).csv"

    confusion_results = r"temp_csv/confusion_results (3) (1).csv"
    importance_features = r"temp_csv/important_features (1) (1).csv"

    metrics_reults = r"temp_csv/metrics_results (3) (1).csv"
    models_result = r"temp_csv/models_result (13) (1).csv"


class prediction_link(Enum):
    PREDICTION = r"temp_csv/heart_statlog_cleveland_hungary_final (8) (1).csv"


class DestinationDatabase(Enum):
    SCHEMA_NAME = "dw_reporting"
    DATABASE_NAME = "heart_db"


class ETL_CHECK_POINT_TABLE(Enum):
    ETL_CHECKPOINT = "etl_checkpoint"


class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"
    POSTHOOK = "posthook"


class ML_TYPE:
    NON_LINEAR = "NON_LINEAR_ML"
    LINEAR_ML = "LINEAR_ML"


class ChestPainType(Enum):
    TYPICAL_ANGINA = 1
    ATYPICAL_ANGINA = 2
    NON_ANGINAL_PAIN = 3
    ASYMPTOMATIC = 4


class RestECGType(Enum):
    NORMAL = 0
    ST_T_WAVE_ABNORMALITY = 1
    LEFT_VENTRICULAR_HYPERTROPHY = 2


class StSlopeType(Enum):
    UPSLOPING = 1
    FLAT = 2
    DOWNSLOPING = 3


class SexType(Enum):
    FEMALE = 0
    MALE = 1


class Output_Directory(Enum):
    CSV = "csv"
