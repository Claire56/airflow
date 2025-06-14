# ✈️ Aircraft Landing Safety - Model Evaluation Pipeline

This project demonstrates a robust and scalable machine learning evaluation pipeline using **Apache Airflow** and **MLFlow**, simulating a real-world safety-critical use case: **predicting safe aircraft landings** from flight telemetry.

---

## 📦 Features

- ✅ Automated data ingestion and preprocessing
- ✅ Training a `RandomForestClassifier` on aircraft landing data
- ✅ Logging model artifacts and metrics to **MLFlow**
- ✅ Modular, scalable DAG powered by **Airflow**
- ✅ Easily extensible to include robustness, uncertainty, and synthetic data tests

---

## 🛠️ Stack

| Component       | Purpose                              |
|----------------|--------------------------------------|
| **Airflow**     | Workflow orchestration               |
| **MLFlow**      | Experiment tracking & model registry |
| **Docker Compose** | Containerized local development     |
| **scikit-learn**| ML training and evaluation           |
| **Pandas**      | Data preprocessing                   |

---

## 🚀 Getting Started

### 1. 📁 Folder Structure


├── dags/<br>
│ └── aircraft_eval_dag.py # Airflow DAG <br>
├── data/<br>
│ └── aircraft_landing_data.csv # Sample telemetry data<br>
├── Dockerfile.airflow-mlflow # Custom Airflow image with MLFlow<br>
├── docker-compose.yml # Full stack: Airflow, MLFlow, DBs<br>
└── mlruns/ # MLFlow tracking artifacts<br>


---

### 2. 🐳 Run the Stack

```bash
# Build and start all services
docker-compose up --build
```
### Access UIs:
Airflow: http://localhost:8080 <br>
→ Login: airflow / airflow<br>

MLFlow: http://localhost:5500<br>

### 3. 🧪 Run the Pipeline
1. Open Airflow UI

2. Enable and trigger the DAG: mlflow_aircraft_landing_eval

3. View logs and metrics in MLFlow UI

📊 Sample Logged Metrics<br>
#### Metric	Description
Accuracy:	Model's performance on test split<br>
Artifacts:	Trained model with metadata<br>
Versioning:	Each run logged with MLFlow experiment<br>

### You can extend this pipeline with:

* Robustness tests (e.g., fog simulation, occlusion)

* SHAP/LIME explainability modules

* Uncertainty estimation (MC Dropout, ensembles)

🧹 Cleanup
```bash
docker-compose down -v
```

📝 Notes
* MLFlow experiment logs are stored under ./mlruns

* Default dataset is synthetic. You can plug in real telemetry from flight simulations.

* Ensure Docker has at least 4GB RAM to prevent worker crashes or out-of-memory issues.

* You can customize your Airflow container using the Dockerfile.airflow-mlflow






