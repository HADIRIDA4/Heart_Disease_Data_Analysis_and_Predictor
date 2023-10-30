CREATE TABLE IF NOT EXISTS target_schema.dim_disease_category (

    ID BIGINT PRIMARY KEY,
    Name TEXT,
    Level BIGINT,
    date_added TIMESTAMP
);


INSERT INTO target_schema.dim_disease_category (ID, Name, Level, date_added)
SELECT ID, Name, Level, date_added FROM target_schema.stg_heart_db_disease_category
ON CONFLICT (ID) DO Nothing
