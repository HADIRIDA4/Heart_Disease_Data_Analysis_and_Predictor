CREATE TABLE IF NOT EXISTS target_schema.dim_cleveland_study
(
  ID bigint primary key not null,
  General_Health text,
  Checkup text,
  Exercise varchar(255),
  Heart_Disease varchar(255),
  Skin_Cancer varchar(255),
  Other_Cancer varchar(255),
  Depression varchar(255),
  Diabetes varchar(255),
  Arthritis varchar(255),
  Sex text,
  Age_Category text,
  Height numeric,
  Weight numeric,
  BMI numeric,
  Smoking_History varchar(255),
  Alcohol_Consumption int,
  Fruit_Consumption int,
  Green_Vegetables_Consumption int,
  FriedPotato_Consumption int,
  last_update timestamp
);


INSERT INTO target_schema.dim_cleveland_study
(
  SELECT 
    ID_,
    General_Health,
    Checkup,
    Exercise,
    Heart_Disease,
    Skin_Cancer,
    Other_Cancer,
    Depression,
    Diabetes,
    Arthritis,
    Sex,
    Age_Category,
    Height,
    Weight,
    BMI,
    Smoking_History,
    Alcohol_Consumption,
    Fruit_Consumption,
    Green_Vegetables_Consumption,
    FriedPotato_Consumption,
    last_update
  FROM target_schema.stg_heart_db_cleveland
)

