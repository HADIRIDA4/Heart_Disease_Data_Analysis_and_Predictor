-- Create the target table
CREATE TABLE IF NOT EXISTS target_schema.agg_top_models
(
  Model TEXT,
  Accuracy FLOAT,
  Precision FLOAT,
  Sensitivity FLOAT,
  Specificity FLOAT,
  F1_Score FLOAT,
  ROC FLOAT,
  Log_Loss FLOAT,
  Mathew_CorrCoef FLOAT,
  RMSE FLOAT,
  last_update TIMESTAMP
);
Insert into target_schema.agg_top_models
(
SELECT  
Model ,
  Accuracy ,
  Precision ,
  Sensitivity ,
  Specificity ,
  F1_Score ,
  ROC ,
  Log_Loss ,
  Mathew_CorrCoef ,
  RMSE ,
  last_update
  from target_schema.stg_heart_db_model_result_csv_path

) 