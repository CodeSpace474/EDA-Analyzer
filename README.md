# EDA-Analyzer
Performs simple Exploratory Data Analysis (EDA) on small datasets
## 📊 EDA Analyzer & AutoML Reporter
An end-to-end Automated Exploratory Data Analysis (EDA) and Machine Learning pipeline built with Streamlit.
This tool transforms raw CSV data into a professional, insight-driven .docx report and a deployment-ready predictive model with just a few clicks.
## 🌟 Key Features
### One-Click EDA
Automatically generates missing value analysis, correlation heatmaps, and target distribution plots.
### Smart Preprocessing
Handles numerical scaling, categorical encoding (One-Hot), and missing value imputation out of the box using Scikit-Learn pipelines.
### AutoML Engine
Compares multiple algorithms (Random Forest, Linear/Logistic Regression, Decision Trees) and selects the best performer based on $R^2$ or F1-Score.
### Feature Engineering
Automatically drops high-correlation features ($>0.9$) to prevent multi-collinearity and improve model stability.
### Explainable AI (XAI)
Integrated SHAP values and Permutation Importance to visualize which features truly drive your model's decisions.
### Automated Docx Reporting
Exports a full technical report including tables, charts, and AI-based recommendations to a Microsoft Word document.
### 🛠️ Installation
1. Clone the Repository
2. Install Dependencies
3. Make sure you have Python 3.8+ installed.
4. It is recommended to use a virtual environment.
5. CMD -> pip install -r requirements.txt
## 🚀 How to Use
### Method 1
CMD -> streamlit run EDA_Analyzer.py
### Method 2
If you are on Windows, you can use the EDA_Launcher.py to start the server and open your browser automatically.
### Note: Open EDA_Launcher.py and ensure the PYTHON_PATH variable matches your local Python installation path.
## 📂 Project Structure
1. EDA_Analyzer.py: The main application logic (UI, Data Processing, AutoML).
2. EDA_Launcher.py: A helper script for silent startup and browser automation.
3. OUTPUT_YYYYMMDD_HHMMSS/: (Auto-generated) Each run creates a unique folder containing your plots, the trained model.pkl, and the final EDA_REPORT.docx.
## 📊 Technical Overview
The pipeline follows a standard data science lifecycle:
### Data Ingestion
Upload CSV via Streamlit
### Statistical Analysis
Calculation of Skewness, Kurtosis, and Cardinality
### Visualization
Seaborn and Matplotlib used for statistical plotting.
### Model Selection
Scikit-Learn Pipeline and ColumnTransformer for robust cross-validation
### Interpretation
Permutation Importance and SHAP summary plots for model transparency.
## 📝 Requirements
Python 3.11+
Streamlit
Pandas
NumPy
Scikit-Learn
SHAP
Python-Docx
Joblib
## 🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests to improve the AutoML logic or reporting templates!
