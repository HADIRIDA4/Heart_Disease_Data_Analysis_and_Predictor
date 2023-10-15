CREATE TABLE IF NOT EXISTS target_schema.dim_disease
(
  code bigint primary key not null,
  disease_name text, 
  description text 

);
Insert Into target_schema.dim_disease
(
  SELECT 
    code,
    disease_name,
    description


from target_schema.stg_heart_db_disease
)
ON conflict (code)
DO update set 
  code=EXCLUDED.code,
  disease_name=EXCLUDED.disease_name,
  description=EXCLUDED.description;

  