CREATE TABLE IF NOT EXISTS target_schema.fct_incidence_global
(
  location text,
  sex text,
  age_interval text,
  cause_id bigint,
  year numeric,
  val numeric,
  last_update timestamp
);



INSERT INTO target_schema.fct_incidence_global
(
  SELECT
    location,
    sex,
    age_interval,
    cause_id,
    year,
    val,
    last_update
  FROM target_schema.stg_heart_db_incidence_global
)

