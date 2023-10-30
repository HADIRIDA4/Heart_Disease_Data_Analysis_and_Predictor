CREATE TABLE IF NOT EXISTS target_schema.dim_framingham_study
(
  RANDID  BIGINT ,
  SEX BIGINT,
  TOTCHOL INT,
  AGE INT,
  SYSBP INT  ,
  DIABP INT ,
  CURSMOKE INT,
  CIGPDAY INT,
  BMI FLOAT,
  DIABETES INT,
  BPMEDS INT,
  HEARTRTE FLOAT,
  GLUCOSE INT,
  educ INT,
  PREVCHD INT,
  PREVAP INT,
  PREVMI INT,
  PREVSTRK INT,
  PREVHYP INT,
  TIME INT,
  PERIOD INT,
  HDLC INT,
  LDLC INT,
  DEATH Int,
  ANGINA Int,
  HOSPMI Int,
  MI_FCHD Int,
  ANYCHD Int,
  STROKE Int,
  CVD INT,
  HYPERTEN INT,
  TIMEAP numeric,
  TIMEMI numeric,
  TIMEMIFC numeric,
  TIMECHD numeric,
  TIMESTRK numeric,
  TIMECVD numeric,
  TIMEDTH numeric,
  TIMEHYP numeric,
  date_added timestamp
);

-- Insert new records while avoiding redundancy based on all attributes
INSERT INTO target_schema.dim_framingham_study (
    RANDID, SEX, TOTCHOL, AGE, SYSBP, DIABP, CURSMOKE, CIGPDAY, BMI,
    DIABETES, BPMEDS, HEARTRTE, GLUCOSE, educ, PREVCHD, PREVAP, PREVMI, PREVSTRK,
    PREVHYP, TIME, PERIOD, HDLC, LDLC, DEATH, ANGINA, HOSPMI, MI_FCHD, ANYCHD, STROKE,
    CVD, HYPERTEN, TIMEAP, TIMEMI, TIMEMIFC, TIMECHD, TIMESTRK, TIMECVD, TIMEDTH, TIMEHYP, date_added
)
SELECT
    s.RANDID, s.SEX, s.TOTCHOL, s.AGE, s.SYSBP, s.DIABP, s.CURSMOKE, s.CIGPDAY, s.BMI,
    s.DIABETES, s.BPMEDS, s.HEARTRTE, s.GLUCOSE, s.educ, s.PREVCHD, s.PREVAP, s.PREVMI, s.PREVSTRK,
    s.PREVHYP, s.TIME, s.PERIOD, s.HDLC, s.LDLC, s.DEATH, s.ANGINA, s.HOSPMI, s.MI_FCHD, s.ANYCHD, s.STROKE,
    s.CVD, s.HYPERTEN, s.TIMEAP, s.TIMEMI, s.TIMEMIFC, s.TIMECHD, s.TIMESTRK, s.TIMECVD, s.TIMEDTH, s.TIMEHYP, s.date_added
FROM target_schema.stg_heart_db_framingham_study AS s
WHERE NOT EXISTS (
    SELECT 1
    FROM target_schema.dim_framingham_study AS t
    WHERE
        s.RANDID = t.RANDID
        AND s.SEX = t.SEX
        AND s.TOTCHOL = t.TOTCHOL
        AND s.AGE = t.AGE
        AND s.SYSBP = t.SYSBP
        AND s.DIABP = t.DIABP
        AND s.CURSMOKE = t.CURSMOKE
        AND s.CIGPDAY = t.CIGPDAY
        AND s.BMI = t.BMI
        AND s.DIABETES = t.DIABETES
        AND s.BPMEDS = t.BPMEDS
        AND s.HEARTRTE = t.HEARTRTE
        AND s.GLUCOSE = t.GLUCOSE
        AND s.educ = t.educ
        AND s.PREVCHD = t.PREVCHD
        AND s.PREVAP = t.PREVAP
        AND s.PREVMI = t.PREVMI
        AND s.PREVSTRK = t.PREVSTRK
        AND s.PREVHYP = t.PREVHYP
        AND s.TIME = t.TIME
        AND s.PERIOD = t.PERIOD
        AND s.HDLC = t.HDLC
        AND s.LDLC = t.LDLC
        AND s.DEATH = t.DEATH
        AND s.ANGINA = t.ANGINA
        AND s.HOSPMI = t.HOSPMI
        AND s.MI_FCHD = t.MI_FCHD
        AND s.ANYCHD = t.ANYCHD
        AND s.STROKE = t.STROKE
        AND s.CVD = t.CVD
        AND s.HYPERTEN = t.HYPERTEN
        AND s.TIMEAP = t.TIMEAP
        AND s.TIMEMI = t.TIMEMI
        AND s.TIMEMIFC = t.TIMEMIFC
        AND s.TIMECHD = t.TIMECHD
        AND s.TIMESTRK = t.TIMESTRK
        AND s.TIMECVD = t.TIMECVD
        AND s.TIMEDTH = t.TIMEDTH
        AND s.TIMEHYP = t.TIMEHYP
        AND s.date_added > t.date_added
);
