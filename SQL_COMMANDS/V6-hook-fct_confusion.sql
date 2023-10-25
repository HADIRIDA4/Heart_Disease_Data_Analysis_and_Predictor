CREATE TABLE IF NOT EXISTS target_schema.fct_CONFUSION_prediction
(
  TN INT,
  FP INT,
  FN INT,
  TP INT,
  last_update timestamp
);

INSERT INTO target_schema.fct_CONFUSION_prediction
(SELECT
  TN,
  FP,
  FN,
  TP,
  last_update
  FROM target_schema.stg_heart_db_confusion_prediction
)

  

