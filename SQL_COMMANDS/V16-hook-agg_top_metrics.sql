-- Create the target table
CREATE TABLE IF NOT EXISTS target_schema.agg_top_metrics_ranking
(
  
  Accuracy FLOAT,
  Precision FLOAT,
  Recall FLOAT,
  F1_Score FLOAT,
  last_update TIMESTAMP
);

-- Insert data into the target table from the source table
INSERT INTO target_schema.agg_top_metrics_ranking
(
  SELECT
    Accuracy,
    Precision,
    Recall,
    F1_Score,
    last_update
  FROM target_schema.stg_heart_db_metrics_ranking
);
