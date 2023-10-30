CREATE TABLE IF NOT EXISTS target_schema.fct_epidemiological_records
(
  measure_id  INT,
  location_ID INT,
  sex_name text,
  age_name text,
  cause_id int,
  metric_name text,
  year INT,
  val float,
  date_added timestamp,
  UNIQUE (measure_id, location_ID, sex_name, age_name, cause_id, metric_name, year)

);



INSERT INTO target_schema.fct_epidemiological_records (
    measure_id, location_ID, sex_name, age_name, cause_id, metric_name, year, val, date_added
)
SELECT
    s.measure_id, s.location_id, s.sex_name, s.age_name, s.cause_id, s.metric_name, s.year, s.val, s.date_added
FROM target_schema.stg_heart_db_epidemiology AS s

ON CONFLICT (measure_id, location_ID, sex_name, age_name, cause_id, metric_name, year) DO NOTHING

