CREATE TABLE IF NOT EXISTS target_schema.fct_global_deaths
(
  location text,
  sex text,
  year int,
  val int,
  last_update timestamp
);

INSERT INTO target_schema.fct_global_deaths
(
  SELECT
  location,
  sex,
  year,
  val,
  last_update
FROM target_schema.stg_heart_db_global_death

)
