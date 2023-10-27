
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
    measure,
    location,
    sex,
    age,
    cause,
    metric,
    year,
    val,
    last_update
  FROM target_schema.stg_heart_db_epidemiology
)

