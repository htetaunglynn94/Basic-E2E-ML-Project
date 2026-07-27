# Basic End-to-End ML Project: Student Performance Predictor

A complete, end-to-end Machine Learning web application designed to predict and analyze student performance based on various demographic and socio-economic factors. 

🔗 **Live Demo:** [https://basic-e2e-ml-project.onrender.com](https://basic-e2e-ml-project.onrender.com)

---

## Project Overview
The goal of this project is to take a machine learning pipeline from raw data exploration all the way to a functional, deployed production web application. 
* **Machine Learning Pipeline:** Includes data ingestion, exploratory data analysis (EDA), data preprocessing/feature engineering, model training, and hyperparameter tuning.
* **Frontend Design:** The web user interface was designed with the assistance of **Gemini AI**, ensuring a clean, modern, and responsive user experience.
* **Deployment:** Hosted live on **Render**.

---

## Project Structure
```text
├── artifacts/           # Saved models, preprocessor objects, and processed datasets
├── catboost_info/       # Training logs for CatBoost models (if applicable)
├── logs/                # Application execution logs
├── notebook/            # Jupyter notebooks for EDA and Model Training
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/            # Raw datasets
├── src/                 # Source code for the ML pipeline and web app
│   ├── components/      # Data ingestion, transformation, and model trainer modules
│   ├── pipeline/        # Prediction and training pipelines
│   ├── exception.py     # Custom exception handling
│   ├── logger.py        # Logging configuration
│   └── utils.py         # Helper functions
├── templates/           # HTML templates for the web frontend (designed with Gemini AI)
├── application.py       # Flask web application entry point
├── Dockerfile           # Containerization configuration
├── requirements.txt     # Python dependencies & Gunicorn web server
└── setup.py             # Setup script for packaging the project
```

---

## Machine Learning Workflow
**Data Ingestion**: Reads the raw student data and splits it into training and testing sets.

**Data Transformation**: Handles missing values, performs feature scaling, and applies categorical encoding using custom pipelines.

**Model Training**: Evaluates multiple machine learning algorithms (such as Random Forest, Gradient Boosting, Linear Regression, CatBoost) to select the best-performing model.

Prediction Pipeline: Loads the trained model and preprocessor artifacts (.pkl) to serve real-time predictions.

---

## Local Installation & Setup
If you want to run the project locally on your machine:

1. Clone the Repository
Bash
git clone [https://github.com/htetaunglynn94/Basic-E2E-ML-Project.git](https://github.com/htetaunglynn94/Basic-E2E-ML-Project.git)
cd Basic-E2E-ML-Project
2. Create a Virtual Environment

```bash
conda create -n mlproject python=3.10 -y
conda activate mlproject
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the Application Locally
```bash
python application.py
```
Open your browser and navigate to http://127.0.0.1:8080.

---

## Run with Docker (Docker Hub)
If you prefer running the pre-built application container directly from Docker Hub without setting up a local Python environment:

```Bash
docker pull htetaunglynn/basic-e2e-ml-project:latest
docker run -p 8080:8080 htetaunglynn/basic-e2e-ml-project:latest
```

---

## Deployment Configuration (Render)
This application is deployed on Render using a Python web service configuration:

Build Command: `pip install -r requirements.txt`

Start Command: `gunicorn application:application`

## Contact

If you have feedback, collaboration opportunities, or professional connections, feel free to reach out.

### 🔗 LinkedIn
https://www.linkedin.com/in/htet-aung-lynn-64ba06146/

### 🔗 GitHub
https://github.com/htetaunglynn94
