CREATE TABLE IF NOT EXISTS target_schema.dim_location (
   location_id BIGINT PRIMARY KEY,
    location_name TEXT,
    date_added TIMESTAMP
);


INSERT INTO target_schema.dim_location (location_id, location_name, date_added)
SELECT  location_id,location_name,  date_added FROM target_schema.stg_heart_db_location
ON CONFLICT (location_id) DO Nothing
