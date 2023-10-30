CREATE TABLE IF NOT EXISTS target_schema.fct_switzerland_study
(
  ID bigint primary key not null,
  HeartDisease char(3),
  BMI float,
  Smoking varchar(3),
  AlcoholDrinking varchar(3) ,
  Stroke varchar(3),
  PhysicalHealth bigint  ,
  MentalHealth bigint  ,
  DiffWalking text,
  Sex text,
  AgeCategory text,
  Race text,
  Diabetic text,
  PhysicalActivity text,
  GenHealth text,
  SleepTime numeric,
  Asthma varchar(3),
  KidneyDisease varchar(3),
  SkinCancer varchar(3),
  last_update timestamp 
);

-- Assuming that your source table is named target_schema.stg_source_table
-- You can adjust the source table name as needed.

INSERT INTO target_schema.fct_switzerland_study
(
  SELECT
    ID,
    HeartDisease,
    BMI,
    Smoking,
    AlcoholDrinking,
    Stroke,
    PhysicalHealth,
    MentalHealth,
    DiffWalking,
    Sex,
    AgeCategory,
    Race,
    Diabetic,
    PhysicalActivity,
    GenHealth,
    SleepTime,
    Asthma,
    KidneyDisease,
    SkinCancer,
    date_added
  FROM target_schema.stg_heart_db_switzerland_study
)
ON CONFLICT (ID) DO NOTHING;

