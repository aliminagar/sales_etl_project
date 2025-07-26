# 📊 SALES_ETL_PROJECT

A professional end-to-end ETL pipeline and interactive dashboard for sales analytics.

---

## 🚀 Features

- Extract, transform, and load (ETL) sales data
- Load data into a SQLite database
- Streamlit-powered interactive dashboard
- CSV download support
- Command-line dashboard version included
- Modular codebase:
  - `extract.py`
  - `transform.py`
  - `load.py`
  - `streamlit_dashboard.py`

---

## 📁 Project Structure

sales_etl_project/
│
├── data/ # Raw and processed data
│ ├── raw_sales_data.csv
│ └── sales.db
│
├── etl/ # Core ETL logic
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── dashboard/ # Dashboards
│ ├── simple_dashboard.py # CLI version
│ └── streamlit_dashboard.py # Streamlit version
│
├── streamlit_env/ # Local Python virtual environment (optional)
├── requirements.txt
└── README.md

---

## ⚙️ How to Run

### 🔹 1. Set Up Environment

python -m venv streamlit_env
streamlit_env\Scripts\activate # On Windows
pip install -r requirements.txt
💡 If requirements.txt doesn’t exist yet, generate it:

pip freeze > requirements.txt
🔹 2. Run the ETL Pipeline

cd etl
python load.py
🔹 3. Launch the Dashboard

cd ..
streamlit_env\Scripts\streamlit run dashboard/streamlit_dashboard.py
🌐 Links
🔗 GitHub Repo: https://github.com/aliminagar/sales_etl_project

💼 LinkedIn: linkedin.com/in/alireza-minagar-md-mba-ms-biotech-bioinformatics-b450aa173

📧 Email: aminagar@gmail.com

🧠 About the Author
Dr. Alireza Minagar
Neurologist | Neuro-immunologist | Bioinformatics Scientist | Full-Stack Software Engineer
Final Project – TripleTen Bootcamp
MS in Software Engineering – University of Maryland Global Campus

Passionate about building data-driven solutions that merge medicine, science, and technology.

```

```
