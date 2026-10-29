
# Customer Churn Intelligence Platform

## Project Overview
This project analyzes customer churn data and uses machine learning
to estimate whether a customer may leave a telecom service.

It includes data cleaning, exploratory data analysis, SQL analysis,
data visualization, machine learning model comparison, and a
Streamlit application for churn prediction.

## Objectives
- Understand customer churn patterns.
- Identify customer characteristics associated with churn.
- Compare Logistic Regression and Random Forest models.
- Predict churn probability for an individual customer.
- Present insights through a dashboard.

## Technology Stack
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- SQLite and SQL
- Streamlit

## Project Structure
- `data/raw/` - Original dataset
- `data/processed/` - Cleaned data and SQLite database
- `src/` - Data preparation, analysis, visualization, and training scripts
- `models/` - Trained model and model comparison results
- `dashboard/` - Churn analytics dashboard
- `app/` - Customer churn prediction application

## Model Evaluation

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 73.81% | 50.43% | 78.34% | 61.36% | 84.16% |
| Random Forest | 77.00% | 55.90% | 63.37% | 59.40% | 82.25% |

Logistic Regression achieved higher recall, F1 score, and ROC-AUC.
Random Forest achieved higher accuracy and precision.

The preferred model depends on the business objective and the cost
of missing customers who are likely to churn.

## Run the Project

1. Create and activate a Python virtual environment.
2. Install the required libraries.
3. Run the prediction application:

   `python -m streamlit run app/app.py`

4. To run the analytics dashboard:

   `python -m streamlit run dashboard/analysis_dashboard.py`

## Dataset
The project uses the IBM Telco Customer Churn dataset.

## Disclaimer
Predictions are estimates, not guarantees. Model performance on
new customers may differ from the evaluation results.
