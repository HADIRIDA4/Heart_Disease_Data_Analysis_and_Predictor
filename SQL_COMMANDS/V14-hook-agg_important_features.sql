-- Create the target table
CREATE TABLE IF NOT EXISTS target_schema.agg_top_features
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
  last_update TIMESTAMP
);

-- Insert data from the source table into the target table
INSERT INTO target_schema.agg_top_features
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
    last_update
  FROM target_schema.stg_heart_db_feature_importance
);
