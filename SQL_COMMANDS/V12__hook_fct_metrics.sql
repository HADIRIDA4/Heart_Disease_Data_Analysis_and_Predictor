-- Create the target table
CREATE TABLE IF NOT EXISTS dw_reporting.fct_metrics_ranking
(
  model_name TEXT PRIMARY KEY,
  accuracy FLOAT,
  precision FLOAT,
  recall FLOAT,
  f1_score FLOAT,
  date_added TIMESTAMP
);

INSERT INTO dw_reporting.fct_metrics_ranking (model_name, accuracy, precision, recall, f1_score, date_added)
SELECT
  model_name,
  accuracy,
  precision,
  recall,
  f1_score,
  date_added
FROM dw_reporting.stg_heart_db_metrics_reults
ON CONFLICT (model_name) -- Specify the column that causes a conflict
DO UPDATE SET
  accuracy = EXCLUDED.accuracy,
  precision = EXCLUDED.precision,
  recall = EXCLUDED.recall,
  f1_score = EXCLUDED.f1_score,
  date_added = EXCLUDED.date_added;

