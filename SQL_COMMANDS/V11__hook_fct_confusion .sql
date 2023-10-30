CREATE TABLE IF NOT EXISTS target_schema.fct_CONFUSION_prediction
(
  model_name TEXT primary key , 
  TN INT,
  FP INT,
  FN INT,
  TP INT,
  date_added TIMESTAMP
);
INSERT INTO target_schema.fct_CONFUSION_prediction (model_name, TN, FP, FN, TP, date_added)
SELECT model_name, TN, FP, FN, TP, date_added
FROM target_schema.stg_heart_db_confusion_results
ON CONFLICT (model_name) 
DO UPDATE SET
  TN = EXCLUDED.TN,
  FP = EXCLUDED.FP,
  FN = EXCLUDED.FN,
  TP = EXCLUDED.TP,
  date_added = EXCLUDED.date_added;
