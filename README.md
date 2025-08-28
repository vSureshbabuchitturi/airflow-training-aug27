
# 🌬️ Airflow Data Pipeline – Air Quality & Weather

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)  
![Airflow](https://img.shields.io/badge/Apache%20Airflow-2.x-orange?logo=apacheairflow)  
![CI](https://github.com/your-username/airflow-training-aug27/actions/workflows/ci.yml/badge.svg)  

---

## 📌 Project Overview
This project demonstrates a **data pipeline using Apache Airflow** that:
- Fetches **air quality data** (PM2.5) from OpenAQ 🌍
- Fetches **weather data** ☀️🌧️  
- Stores data in **Parquet or CSV format**  
- Can be extended for **data transformations and analytics**  

---

## 📂 Repository Structure


airflow-training-aug27/
│── etl/
│ ├── ingest.py # Fetch data from APIs
│ ├── transform.py # (Future) Data cleaning & transformation
│ └── load.py # (Future) Store into DB/warehouse
│
│── dags/
│ └── pipeline_dag.py # Airflow DAG definition
│
│── pipeline.py # CLI pipeline runner
│── requirements.txt # Python dependencies
│── .github/workflows/
│ └── ci.yml # CI/CD pipeline config
│── README.md # Project documentation


---

## ⚙️ Installation & Setup
### 🔹 Prerequisites
- Python **3.10+** (tested on 3.13 ✅)  
- Apache Airflow installed  
- GitHub Actions (for CI/CD)  

### 🔹 Setup Instructions
```bash
# Clone the repository
git clone https://github.com/your-username/airflow-training-aug27.git
cd airflow-training-aug27

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt

▶️ Running the Pipeline

Run directly from CLI:

python pipeline.py --fmt parquet


Options:

--fmt parquet → saves data in Parquet format

--fmt csv → saves data in CSV format

⏳ Running with Airflow

Place pipeline_dag.py inside your Airflow dags/ folder.

Start Airflow webserver & scheduler:

airflow db init
airflow webserver -p 8080
airflow scheduler


Open http://localhost:8080
 🌐

Enable and trigger the DAG ✅

✅ Continuous Integration (CI)

This project uses GitHub Actions to:

Run linting (flake8)

Run tests (pytest)

Check pipeline execution

Workflow file: .github/workflows/ci.yml

📊 Future Enhancements

 Add transformations (cleaning, aggregations)

 Load into a database (Postgres / BigQuery / Snowflake)

 Add anomaly detection on air quality data

 Build dashboards with Superset / Power BI / Looker

🤝 Contributing

Pull requests are welcome!
Please follow PEP8
 and ensure tests pass before submitting.

📜 License

MIT License © 2025 [Your Name]


⚡ This is a **ready-to-paste README.md** with:  
✔️ Badges  
✔️ Emojis  
✔️ Code blocks  
✔️ Sections (Setup, Running, CI, Future work)  

👉 Do you also want me to **write the GitHub Actions `ci.yml` file** so it run
