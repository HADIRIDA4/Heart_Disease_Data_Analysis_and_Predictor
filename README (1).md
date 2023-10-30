<img  src="readme\title1.svg"/>

<div>

> Hello world! This is the project’s summary that describes the project, plain and simple, limited to the space available.
> **[PROJECT PHILOSOPHY](#project-philosophy) • [PROTOTYPING](#prototyping) • [TECH STACKS](#stacks) • [IMPLEMENTATION](#demo) • [HOW TO RUN?](#run)**

</div>

<br><br>

<!-- project philosophy -->

<a  name="philosophy" ></a>
<img  src="readme/title2.svg" id="project-philosophy"/>

> A Python-based ETL (Extract, Transform, Load) project aimed at processing data from various web sources, and subsequently storing it in a tabular database (PostgreSQL), with the objective of facilitating comprehensive analysis Disease disease data

> Heart Disease Analysis and Predictor Project, also aims to predict the probabilities if this might occur in the near future based on the data analyzed.<br>

### User Types

1. Healthcare Practitioners
2. Policy Makers.
3. Data Analysts and Scientists.
4. Policy Makers.
5. Journalist.

<br>

Healthcare Practitioners:

Interested in project insights to improve patient care, identify at-risk populations, and enhance clinical decision-making.
Use findings for early intervention and personalized treatment strategies.
Benefit from understanding disease trends to allocate resources effectively.
Policy Makers:

Utilize project data to inform evidence-based public health policies and initiatives.
Address disease prevalence, risk factors, and preventive measures.
Make informed decisions to enhance community health outcomes.
Data Analysts and Scientists:

Analyze data for research, modeling, and in-depth understanding of cardiovascular disease trends.
Develop predictive models to identify risk factors and potential interventions.
Contribute to scientific advancements in the field.
Public Health Officials:

Leverage project insights for public health campaigns and interventions.
Prioritize resource allocation for prevention and awareness programs.
Monitor and respond to changing disease patterns effectively.
General Public:

Gain knowledge about cardiovascular disease risks and prevention.
Make informed lifestyle choices to reduce the risk of heart-related conditions.
Understand the impact of heart health on personal well-being.

### User Stories

1.  Healthcare Practitioners:

    I want to access project insights to improve patient care, identify at-risk populations, and enhance clinical decision-making.
    I want to use findings for early intervention and personalized treatment strategies.
    I want to benefit from understanding disease trends to allocate resources effectivelys.

2.  Policy Makers:

    I want to utilize project data to inform evidence-based public health policies and initiatives.
    I want to address disease prevalence, risk factors, and preventive measures.
    I want to make informed decisions to enhance community health outcomes.

3.  Data Analysts and Scientists:

    I want to analyze data for research, modeling, and in-depth understanding of cardiovascular disease trends.
    I want to develop predictive models to identify risk factors and potential interventions.
    I want to contribute to scientific advancements in the field.

4.  Public Health Officials:

    I want to leverage project insights for public health campaigns and interventions.
    I want to prioritize resource allocation for prevention and awareness programs.
    I want to monitor and respond to changing disease patterns effectively.

5.  General Public:

    I want to gain knowledge about cardiovascular disease risks and prevention.
    I want to make informed lifestyle choices to reduce the risk of heart-related conditions.
    I want to understand the impact of heart health on personal well-being.

<br><br>

<!-- Prototyping -->
<img  src="readme\title3.svg"  id="prototyping"/>

> We have designed our projects to webscrape, through an ETL project and including it in a PowerBI Sample Dashboard,

### Logger File

| Bins Map screen | Dashboard screen | Bin Management screen |

| ---| ---| ---|

| ![Landing](./readme/wireframes/web/map.png) | ![Admin Dashboard](./readme/wireframes/web/dashboard.png) | ![User Management](./readme/wireframes/web/bin_crud.png) |

### Data Flow Diagrams

<img  src="readme\Copy of db_Heart.png"  id="prototyping"/>
<br><br>

<!-- Tech stacks -->

<a  name="stacks"></a>
<img  src="readme/title4.svg" id="stacks" />

<br>

Bin Tracker is built using the following technologies:

## Frontend

Interactive PowerBI Dashboard:
A central dashboard where viewers can view:

1. Epidemiological Indicators: Graphs, charts and visualizations displaying key Health metrics over time.
2. Cohort Studies Analysis:Cohort Studies Analysis: Conduct comprehensive analysis of cohort studies to investigate trends, risk factors, and outcomes in a defined group over time, providing valuable insights into the factors influencing specific health or research outcomes.
3. Predictive Analysis: A visualization of the ML model's performance about occurence of disease compared to actual data.
4. Interactive filters: options to filter data by date, region,type of disease,sex, or specific economic indicatiors for customized views.

<br>

## Backend

1. Automation.
2. ETL Pipeline: using python and pandas, raw data is extracted, transformed into a usable format and loaded into postgreSQL database.
3. Database: Schema Design - Data Integrity - Backup & Recovery.
4. Machine Learning & Predictive Analysis: Model Training - Evaluation and Prediction.

<br>

<br>

<!-- Implementation -->

<a  name="Demo"  ></a>
<img  src="readme\title5.svg" id="#demo"/>

> Show command line of ETL performance - Logger view

### App

| Dashboard Screen | Create Bin Screen |

| ---| ---|

| ![Landing](./readme/implementation/dashboard.gif) | ![fsdaf](./readme/implementation/create_bin.gif) |

| Bins to Map Screen |

| ---|

| ![fsdaf](./readme/implementation/map.gif) |

| Filter Bins Screen | Update Pickup Time Screen |

| ---| ---|

| ![Landing](./readme/implementation/filter_bins.gif) | ![fsdaf](./readme/implementation/update_pickup.gif) |

| Announcements Screen |

| ---|

| ![fsdaf](./readme/implementation/message.gif)|

| Change Map Screen | Edit Profile Screen |

| ---| ---|

| ![Landing](./readme/implementation/change_map.gif) | ![fsdaf](./readme/implementation/edit_profile.gif) |

| Landing Screen |

| ---|

| ![fsdaf](./readme/implementation/landing.gif)|

<br><br>

### Machine Learning (ML) component

Using sickit-learn, we analyze the health data, training predictive models and deploying them for real-time predictions.

Data Collection & Preprocessing.
Model Selection & Training
Model Evaluation.
Model Deployment

| ML Flow Diagram|

| ---| ---|

|![fsdaf](./readme/implementation/arduino.gif)|![fsdaf](./readme/implementation/circuit.png)

| Data Transfer Demo |

| ---|

| ![fsdaf](./readme/implementation/arduino_data.png) |

<br><br>

<!-- How to run -->

<a  name="run"  ></a>
<img  src="readme\title6.svg" id="run"/>

> To set up ## **Heart Disease and Predictor** follow these steps:

### Prerequisites

**Hardware & Software**:

- A computer/server with sufficient RAM (minimum 8gb ram) and processing power.
- Operating system: Linux (preferred for production) or Windows.
- Required software: Python (3.x), PostgreSQL, Git (for version control), and any other specific software packages.

**Dependencies**:

- Install the necessary Python libraries: `pandas`, `scikit-learn`, `numpy`, `xgboost`.
- Install database connectors/drivers for PostgreSQL.

### **Setting Up the Environment**:

**Clone the Repository**:

```sh

git clone https://github.com/HADIRIDA4/Heart_Disease_Data_Analysis_and_Predictor

```

**Set Up the Database**:

- Start the PostgreSQL server.
- Create a new database and user with the appropriate permissions.
- Run any initialization scripts to set up tables or initial.

### **Running the Backend**:

**Start the Data Ingestion & ETL Process**:
`python data_ingestion_script.py`

You should be able to check the app.log file to see the ETL work.

As for the dashboard access: Please use this link "public powerbi link" to access your data.
