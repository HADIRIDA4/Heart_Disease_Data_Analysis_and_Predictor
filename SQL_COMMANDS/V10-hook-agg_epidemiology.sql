
CREATE TABLE IF NOT EXISTS target_schema.fct_epidemiology
(
  measure text,
  location_name text,
  sex text,
  age_interval text,
  cause text,
  metric text,
  year INT,
  val float,
  last_update timestamp
);


INSERT INTO target_schema.fct_epidemiology
(
  SELECT
    stg.measure,
    stg.location,
    stg.sex,
    stg.age,
    stg.cause,
    stg.metric,
    stg.year,
    stg.val,
    stg.last_update
  FROM target_schema.stg_heart_db_epidemiology stg
)

ON CONFLICT (last_update)
DO UPDATE SET
  val = EXCLUDED.val;
