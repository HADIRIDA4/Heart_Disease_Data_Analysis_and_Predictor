CREATE TABLE IF NOT EXISTS target_schema.dim_disease (
    cause_id BIGINT PRIMARY KEY,
    cause_name TEXT,
    parent_id INT,
    date_added TIMESTAMP
);


INSERT INTO target_schema.dim_disease (cause_id, cause_name, parent_id, date_added)
SELECT  cause_id,cause_name, parent_id, date_added FROM target_schema.stg_heart_db_disease
ON CONFLICT (cause_id) DO Nothing
