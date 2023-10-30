CREATE TABLE IF NOT EXISTS target_schema.dim_measures (
   measure_id BIGINT PRIMARY KEY,
    number TEXT,
    percent text,
    rate text,
    date_added timestamp
);


INSERT INTO target_schema.dim_measures (
SELECT  measure_id,number,percent,rate,date_added FROM target_schema.stg_heart_db_measures)
ON CONFLICT (measure_id) DO Nothing