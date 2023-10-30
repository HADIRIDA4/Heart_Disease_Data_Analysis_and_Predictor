-- Create the target table
CREATE TABLE IF NOT EXISTS target_schema.fct_top_models
(
  Model  TEXT primary key,
  Accuracy FLOAT,
  Precision FLOAT,
  Sensitivity FLOAT,
  Specificity FLOAT,
  F1_Score FLOAT,
  ROC FLOAT,
  Log_Loss FLOAT,
  Mathew_CorrCoef FLOAT,
  RMSE FLOAT,
  date_added TIMESTAMP
);
INSERT INTO target_schema.fct_top_models (Model, Accuracy, Precision, Sensitivity, Specificity, F1_Score, RMSE,date_added)
SELECT
  Model,
  Accuracy,
  Precision,
  Sensitivity,
  Specificity,
  F1_Score,
  RMSE,
  date_added
FROM target_schema.stg_heart_db_models_result
ON CONFLICT (Model) -- Specify the column that causes a conflict
DO UPDATE SET
  Accuracy = EXCLUDED.Accuracy,
  Precision = EXCLUDED.Precision,
  Sensitivity = EXCLUDED.Sensitivity,
  Specificity = EXCLUDED.Specificity,
  F1_Score = EXCLUDED.F1_Score,
  RMSE = EXCLUDED.RMSE,
  date_added = EXCLUDED.date_added;
