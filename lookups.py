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
    DISEASE_CATEGORY = (
        "https://drive.google.com/uc?id=1wKg3cAFfZPPF36Li-MQX-EEA7ZLXT_wv"
    )
    DISEASE = "https://drive.google.com/uc?id=1CCTSodS_A6XcCXKTkbcRy__H33X5NAID"
    EPIDEMIOLOGY = "https://drive.google.com/uc?id=1ujGL5F3V7PMaYSo7BtJ0AGHX2kgJg_3m"
    FRAMINGHAM_STUDY = (
        "https://drive.google.com/uc?id=1--HEe4xJgPP2EAE-2V8WC3l0WBqBVI_f"
    )
    LOCATION = "https://drive.google.com/uc?id=13KvsA8rPVHiYtyyI9wTTGymFjnMk5u3j"
    MEASURES = "https://drive.google.com/uc?id=1BpEenYp0pZw0DAEajMJV39a-_A_IpRew"
    SWITZERLAND_STUDY = (
        "https://drive.google.com/uc?id=1XF9GZjP5xw1jjUCx3FhVT3AHPs2DbiY4"
    )
    CVD_CLEANED = "https://drive.google.com/uc?id=11yBqPXzNcOIfcgKtlCgMX8i4fno3OIq9"
    confusion_results = (
        "https://drive.google.com/uc?id=1itIYB75d0Su-46Ng59aqcGFiYxiJFZkU"
    )
    importance_features = (
        "https://drive.google.com/uc?id=1DKCnrDq1IwHO6Ln10Ip6SY9nelz56rf0"
    )
    metrics_reults = "https://drive.google.com/uc?id=15gxFEZZBPmj-_5giz1Ncv-k8ra7sdJ9s"
    models_result = "https://drive.google.com/uc?id=12n4-FkXppt34uOgLVvgXiKVPm8O0nnAk"


class prediction_link(Enum):
    PREDICTION = "https://drive.google.com/uc?id=1ZngQXrwS7xxxq-Yjp_tJtgY-2c5l9tr3"


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
