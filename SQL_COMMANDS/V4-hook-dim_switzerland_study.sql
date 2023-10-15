CREATE TABLE IF NOT EXISTS target_schema.dim_switzerland_study
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

INSERT INTO target_schema.dim_switzerland_study
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
    last_update
  FROM target_schema.stg_heart_db_switzerland
)
ON CONFLICT (ID)
DO UPDATE SET
  ID = EXCLUDED.ID,
  HeartDisease = EXCLUDED.HeartDisease,
  BMI = EXCLUDED.BMI,
  Smoking = EXCLUDED.Smoking,
  AlcoholDrinking = EXCLUDED.AlcoholDrinking,
  Stroke = EXCLUDED.Stroke,
  PhysicalHealth = EXCLUDED.PhysicalHealth,
  MentalHealth = EXCLUDED.MentalHealth,
  DiffWalking = EXCLUDED.DiffWalking,
  Sex = EXCLUDED.Sex,
  AgeCategory = EXCLUDED.AgeCategory,
  Race = EXCLUDED.Race,
  Diabetic = EXCLUDED.Diabetic,
  PhysicalActivity = EXCLUDED.PhysicalActivity,
  GenHealth = EXCLUDED.GenHealth,
  SleepTime = EXCLUDED.SleepTime,
  Asthma = EXCLUDED.Asthma,
  KidneyDisease = EXCLUDED.KidneyDisease,
  SkinCancer = EXCLUDED.SkinCancer,
  last_update = EXCLUDED.last_update;
