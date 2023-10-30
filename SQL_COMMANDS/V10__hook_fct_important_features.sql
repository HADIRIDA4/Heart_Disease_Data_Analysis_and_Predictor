-- Create the target table
CREATE TABLE IF NOT EXISTS target_schema.fct_features
(
  age FLOAT,
  resting_bp_s FLOAT,
  cholesterol FLOAT,
  fasting_blood_sugar FLOAT,
  max_heart_rate FLOAT,
  exercise_angina FLOAT,
  oldpeak FLOAT,
  sex_MALE FLOAT,
  chest_pain_type_ATYPICAL_ANGINA FLOAT,
  chest_pain_type_NON_ANGINAL_PAIN FLOAT,
  chest_pain_type_TYPICAL_ANGINA FLOAT,
  resting_ecg_NORMAL FLOAT,
  resting_ecg_ST_T_WAVE_ABNORMALITY FLOAT,
  ST_slope_FLAT FLOAT,
  ST_slope_UPSLOPING FLOAT,
    model  text primary key ,
  date_added TIMESTAMP

);


INSERT INTO target_schema.fct_features
(
  SELECT
    age,
    resting_bp_s,
    cholesterol,
    fasting_blood_sugar,
    max_heart_rate,
    exercise_angina,
    oldpeak,
    sex_MALE,
    chest_pain_type_ATYPICAL_ANGINA,
    chest_pain_type_NON_ANGINAL_PAIN,
    chest_pain_type_TYPICAL_ANGINA,
    resting_ecg_NORMAL,
    resting_ecg_ST_T_WAVE_ABNORMALITY,
    ST_slope_FLAT,
    ST_slope_UPSLOPING,
    model,
    date_added
  FROM target_schema.stg_heart_db_importance_features
)
ON CONFLICT (model) 
DO UPDATE SET
  age = EXCLUDED.age,
  resting_bp_s = EXCLUDED.resting_bp_s,
  cholesterol = EXCLUDED.cholesterol,
  fasting_blood_sugar = EXCLUDED.fasting_blood_sugar,
  max_heart_rate = EXCLUDED.max_heart_rate,
  exercise_angina = EXCLUDED.exercise_angina,
  oldpeak = EXCLUDED.oldpeak,
  sex_MALE = EXCLUDED.sex_MALE,
  chest_pain_type_ATYPICAL_ANGINA = EXCLUDED.chest_pain_type_ATYPICAL_ANGINA,
  chest_pain_type_NON_ANGINAL_PAIN = EXCLUDED.chest_pain_type_NON_ANGINAL_PAIN,
  chest_pain_type_TYPICAL_ANGINA = EXCLUDED.chest_pain_type_TYPICAL_ANGINA,
  resting_ecg_NORMAL = EXCLUDED.resting_ecg_NORMAL,
  resting_ecg_ST_T_WAVE_ABNORMALITY = EXCLUDED.resting_ecg_ST_T_WAVE_ABNORMALITY,
  ST_slope_FLAT = EXCLUDED.ST_slope_FLAT,
  ST_slope_UPSLOPING = EXCLUDED.ST_slope_UPSLOPING,
  date_added = EXCLUDED.date_added;
