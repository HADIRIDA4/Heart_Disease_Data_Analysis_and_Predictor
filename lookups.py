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


   

class studies(Enum):
    FRAMINGHAM_STUDY = "csv/Framingham_Study.csv"
    SWITZERLAND = "csv/Switzerland.csv"
    CLEVELAND = "csv/CVD_cleaned.csv"
    DISEASE = "csv/Disease.csv"
    CONFUSION_PREDICTION = "csv\confusion_results.csv"
    METRICS_RANKING = "csv\metrics_results.csv"
    FEATURE_IMPORTANCE = "csv\important_features_results.csv"     
    MODEL_RESULT_CSV_PATH = "csv\models_result.csv"
    EPIDEMIOLOGY="csv\epidemiological_data.csv"



class links(Enum):
  DISEASE_CATEGORY ="https://drive.google.com/file/d/11DNcehV12u6YCt_lMpuL5FAP3PuRx3Ri/view?usp=drive_link"
  DISEASE ="https://drive.google.com/file/d/13ms6gD8NdZNo0X8n9NV-ncTX-MDZHAci/view?usp=sharing"
  EPIDEMIOLOGY="https://drive.google.com/file/d/1DxJzOuell6qIxZaSwIrvkjQpU-AXktbu/view?usp=sharing"
  FRAMINGHAM_STUDY="https://drive.google.com/file/d/1Ab5vh45YOEHclEqnMogO9BcYA5_qTkEg/view?usp=sharing"
  CLEVELAND_PREDICTION ="https://drive.google.com/file/d/1ZngQXrwS7xxxq-Yjp_tJtgY-2c5l9tr3/view?usp=drive_link"
  PREDICTION="https://drive.google.com/file/d/1Uo0Kt_oKFL6aI-a_uqV8HfMu1HQ6aXQo/view?usp=sharing"
  LOCATION="https://drive.google.com/file/d/1rIfQRJRXaugRoj1Xw4nYZZS7IYG3-3Jk/view?usp=drive_link"
  MEASURES="https://drive.google.com/file/d/1_fT69Pprh_HwDUWjj0tO4QUCqfn02gjh/view?usp=sharing"
  SWITZERLAND_STUDY="https://drive.google.com/file/d/1xD0DYCNhvqpcYHX3fpoeCKFLqHLenk1f/view?usp=drive_link"
  CVD_CLEANED="https://drive.google.com/file/d/1sSAfmx4jmjBWwgkJ9H7dTylrZu5zKofl/view?usp=drive_link"
  




class DestinationDatabase(Enum):
    SCHEMA_NAME = "dw_reporting"
    DATABASE_NAME = "heart_db"






class ETLStep(Enum):
    PRE_HOOK = "prehook"
    HOOK = "hook"
    POSTHOOK="posthook"


class ML_TYPE:
    NON_LINEAR="NON_LINEAR_ML"
    LINEAR_ML="LINEAR_ML"


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
    CSV="csv"