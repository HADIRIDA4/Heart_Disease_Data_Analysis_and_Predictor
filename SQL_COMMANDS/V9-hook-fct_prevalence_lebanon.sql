CREATE TABLE IF NOT EXISTS target_schema.fct_prevalence_lebanon
(
  location text,
  sex text,
  age_interval text,
  cause_id bigint,
  year numeric,
  val numeric,
  last_update timestamp
);

-- Assuming that your source table is named target_schema.stg_source_table
-- You can adjust the source table name as needed.

INSERT INTO target_schema.fct_prevalence_lebanon
(
  SELECT
    location,
    sex,
    age_interval,
    cause_id,
    year,
    val,
    last_update
  FROM target_schema.stg_heart_db_prevalence_lebanon
)

