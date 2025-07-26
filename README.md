# 📊 SALES_ETL_PROJECT

A professional end-to-end ETL pipeline and interactive dashboard for sales analytics.

---

## 🚀 Features

- Extract, transform, and load (ETL) sales data
- Load to SQLite database
- Streamlit-powered interactive dashboard
- CSV download support
- CLI version included
- Modular codebase (`extract.py`, `transform.py`, `load.py`, `streamlit_dashboard.py`)

---

## 📁 Project Structure

sales_etl_project/
│
├── data/ # Raw and processed data
│ └── raw_sales_data.csv
│ └── sales.db
│
├── etl/ # Core ETL logic
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── dashboard/
│ ├── simple_dashboard.py # CLI dashboard
│ └── streamlit_dashboard.py # Streamlit dashboard
│
├── streamlit_env/ # Local Python virtual environment (optional)
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ How to Run

### 🔹 1. Set Up Environment

```bash
python -m venv streamlit_env
streamlit_env\Scripts\activate
pip install -r requirements.txt
If requirements.txt doesn't exist yet, you can generate it using:

bash
Copy
Edit
pip freeze > requirements.txt
🔹 2. Run ETL Pipeline
bash
Copy
Edit
cd etl
python load.py
🔹 3. Run Dashboard
bash
Copy
Edit
cd ..
streamlit_env\Scripts\streamlit run dashboard/streamlit_dashboard.py
🌐 Links
🔗 GitHub Repo: https://github.com/alirezaminagar/sales_etl_project

💼 LinkedIn: www.linkedin.com/in/alireza-minagar-md-mba-ms-biotech-bioinformatics-b450aa173

📧 Email: aminagar@gmail.com

🧠 About the Author
Dr. Alireza Minagar
Neurologist | Neuro-immunologist | Bioinformatics Scientist | Full-Stack Software Engineer
Final Project - TripleTen Bootcamp | MS in Software Engineering - UMGC
Passionate about building data-driven solutions that merge medicine, science, and technology.
```
