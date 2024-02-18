<img  src="readme\title1.svg"/>

<div>

> Hello world! This is the project’s summary that describes the project, plain and simple, limited to the space available.
> **[PROJECT PHILOSOPHY](#project-philosophy) • [PROTOTYPING](#prototyping) • [IMPLEMENTATION](#demo) • [TECH STACKS](#stacks) • [HOW TO RUN?](#run)**

</div>

<br><br>

<!-- project philosophy -->

<a  name="philosophy" ></a>
<img  src="readme/title2.svg" id="project-philosophy"/>
<B>

> <b>A Python-based ETL (Extract, Transform, Load) project aimed at processing data from various web sources, and subsequently storing it in a tabular database (PostgreSQL), with the objective of facilitating comprehensive analysis of Heart Disease<b>

> <b> Heart Disease Analysis and Predictor Project, also aims to predict the probabilities if this might occur in the near future based on the data analyzed.<b><br>

### User Types

1. Healthcare Practitioners
2. Policy Makers.
3. Data Analysts and Scientists.
4. Public Health Officials.
5. General Public.

<br>

### User Stories

1.  Healthcare Practitioners:

- I want to access project insights to improve patient care, identify at-risk populations, and enhance clinical decision-making.
- I want to use findings for early intervention and personalized treatment strategies.
- I want to benefit from understanding disease trends to allocate resources effectivelys.

2.  Policy Makers:

- I want to utilize project data to inform evidence-based public health policies and initiatives.
- I want to address disease prevalence, risk factors, and preventive measures.
- I want to make informed decisions to enhance community health outcomes.

3.  Data Analysts and Scientists:

- I want to analyze data for research, modeling, and in-depth understanding of cardiovascular disease trends.
- I want to develop predictive models to identify risk factors and potential interventions.
- I want to contribute to scientific advancements in the field.

4.  Public Health Officials:

- I want to leverage project insights for public health campaigns and interventions.
- I want to prioritize resource allocation for prevention and awareness programs.
- I want to monitor and respond to changing disease patterns effectively.

5.  General Public:

- I want to gain knowledge about cardiovascular disease risks and prevention.
- I want to make informed lifestyle choices to reduce the risk of heart-related conditions.
- I want to understand the impact of heart health on personal well-being.

<br><br>

<!-- Prototyping -->

<a  name="prototyping" ></a>
<img  src="readme/title3.svg" id="prototyping"/>

### Logger File

<img  src="readme\logger_2.png"  id="prototyping"/>

### Data Tables Schema

<img  src="readme\Copy of db_Heart.png"  id="prototyping"/>

<br><br>

<!-- Implementation -->

<a  name="Demo"></a>
<img  src="readme/title4.svg" id="#demo" />

<br>

# Power BI Report

## landing Page

<img src= "readme\Landing_Page.png" id="prototyping"/>

## Overview Page

<img src="readme\Overview.png" id="prototyping"/>

## Epidemiology Page

<img src="readme\epidimiology.gif" id="prototyping"/>

## Etiology Page

<img src= "readme\etiology_g.gif" id="prototyping"/>

## Classification and Prediction Page

<img src= "readme\classification_and_evaluating.png" id="prototyping"/>

## Navigation Through Report

<img src="readme\OverView.gif" id="prototyping"  />

<br><br>

<!-- Tech stacks -->

<a  name="Stack"></a>
<img  src="readme\title5.svg" id="stacks"/>

<br><br>

<B>Heart Disease Analytics is built using the following technologies:<B>

## Frontend

<B>Interactive PowerBI Dashboard:
A central dashboard where viewers can view:

1. Epidemiological Indicators: Graphs, charts and visualizations displaying key Health metrics over time.
2. Cohort Studies Analysis: Conduct comprehensive analysis of cohort studies to investigate trends , risk factors, and outcomes in a defined group over time, providing valuable insights into the factors influencing specific health or research outcomes.
3. Predictive Analysis: A visualization of the ML model's performance about occurence of disease compared to actual data.
4. Interactive filters:Options to filter data by date, region,type of disease,sex, or specific economic indicatiors for customized views.<B>

<br>

## Backend

1. Automation.
2. ETL Pipeline: using <B>P<B>ython and <B>P<B>andas, raw data is extracted, transformed into a usable format and loaded into postgreSQL database.
3. Database: Schema Design - Data Integrity - Backup & Recovery.
4. Machine Learning & Predictive Analysis: Model Training - Evaluation and Prediction.

<br>

<br>

<!-- How To Run -->

<a  name="How To Run "  ></a>
<img  src="readme\title6.svg" id="Run"/>

<br><br>

### Prerequisites

**Hardware & Software**:

- A computer/server with sufficient RAM (minimum 8gb ram) and processing power.
- Operating system: Linux (preferred for production) or Windows.
- Required software: Python (3.x), PostgreSQL, Git (for version control), and any other specific software packages.

**Dependencies**:

- Install the necessary Python libraries: `Pandas`, `Scikit-learn`, `Numpy`, `Xgboost`,`Psycopg2`.
- Install database connectors/drivers for PostgreSQL.

### **Setting Up the Environment**:

**Clone the Repository**:

```sh

git clone https://github.com/HadiAlRida/Heart_Disease_Data_Analysis_and_Predictor

```

**Set Up the Database**:

- Start the PostgreSQL server.
- Create a new database and user with the appropriate permissions.g
- Run any initialization scripts to set up tables or initial.

### **Running the Backend**:

**Start the Data Ingestion & ETL Process**:
`python data_ingestion_script.py`

You should be able to check the app.log file to see the ETL work.

**Run the Machine Learning Model**:
`ml_model.py`

- Run this model and you wil be able to get live prediction for your entered Data
  You should be able to check the ML Process and Output file to see Output
- As for the dashboard access: Please use this link "[Public Powerbi Link ](https://app.powerbi.com/view?r=eyJrIjoiMTU4OWJiMDUtNzM0NS00ZGFmLWFhZDEtZmYwYWZjM2NmZjVhIiwidCI6IjJhZDk2OTM0LTQzZTUtNDFjMi05NzYxLWYzMzVmZTIxNGNjMyIsImMiOjl9)" to access your data.
