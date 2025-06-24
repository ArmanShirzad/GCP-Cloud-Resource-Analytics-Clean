
# Cloud Resource Analytics 

A serverless, production-grade GCP dashboard for real-time cloud usage, cost analytics, and cost-saving recommendations—built for rapid demonstration, technical interviews, and hands-on learning.

    +------------------------------+
    | Client (curl/browser/etc.)   |
    +--------------+---------------+
                   |
                   v
    +--------------+---------------+
    | Cloud Run "analytics-api"    |  <-- container built from Dockerfile
    | (FastAPI application)        |
    +--------------+---------------+
                   | queries
                   v
    +--------------+---------------+
    | BigQuery dataset "usage_data"|
    | table "resource_usage"       |
    +------------------------------+

    +------------------------------+
    | Compute Engine VM "demo-vm"  |  <-- small preemptible instance
    +------------------------------+
usage endpoint sample response
![image](https://github.com/user-attachments/assets/4a9b09a0-d389-40c1-897b-0afe5975fa9d)


---

## 🚀 What is this?

**Cloud Resource Analytics Dashboard** is a fully automated solution that:

- Provisions Google Cloud resources (VMs, BigQuery, API endpoints) using Terraform  
- Ingests GCP resource usage/cost data into BigQuery  
- Exposes usage and cost analytics via a FastAPI REST API (served on Cloud Run)  
- Offers cost-saving recommendations (e.g., idle VM detection) based on actual or simulated usage data  
- Designed for the always-free GCP tier (so anyone can run it)

---

## ✨ Features

- **Infrastructure as Code**: Reproducible deployments with Terraform  
- **BigQuery Data Lake**: Stores cloud usage and cost metrics  
- **Python REST API**: FastAPI + OpenAPI docs; endpoints for `/usage`, `/costs`, `/recommendations`  
- **Cost-Saving Insights**: Flags underused resources (idle VMs, etc.)  
- **Modular & Extensible**: Add new endpoints or analytics logic in minutes

---

## 🛠️ Stack

- **Python 3.11** (`FastAPI`, `google-cloud-bigquery`)  
- **Terraform 1.8+** (GCP provider)  
- **Google Cloud Platform**  
  - Compute Engine (VM)  
  - BigQuery (dataset, table)  
  - Cloud Run (serverless API hosting)  
  - IAM (principle of least privilege)

---

## 📦 Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/armanshirzad/GCP-Cloud-Resource-Analytics.git


2. **Set up GCP project** (with billing & BigQuery export enabled)

3. **Configure and apply Terraform**

   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

4. **Build & push the API image**

   ```bash
   docker build -t gcr.io/<your-project-id>/analytics-api:v1 .
   docker push gcr.io/<your-project-id>/analytics-api:v1
   ```

5. **Deploy on Cloud Run** (or via Terraform):

   ```bash
   gcloud run services update analytics-api \
     --region=us-central1 \
     --image=gcr.io/<your-project-id>/analytics-api:v1 \
     --update-env-vars=BQ_DATASET=usage_data,BQ_TABLE=resource_usage
   ```

6. **Insert mock data** (for demo/testing):

   ```sql
   INSERT INTO `your-project.usage_data.resource_usage`
     (timestamp, project_id, service, resource, usage_amount, cost_usd)
   VALUES
     (TIMESTAMP("2025-06-20 18:45:00"), "your-project", "Compute Engine", "demo-vm", 5.2, 0.15),
     (TIMESTAMP("2025-06-20 18:46:00"), "your-project", "Cloud Run", "analytics-api", 1.3, 0.04);
   ```

7. **Open the API**
   [https://analytics-api-xxxxxx.a.run.app/docs](https://analytics-api-xxxxxx.a.run.app/docs) (see live Swagger docs)

---

## 🌐 API Endpoints

| Method | Path               | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/usage`           | Usage by service and day  |
| GET    | `/costs`           | Cost breakdown by service |
| GET    | `/recommendations` | Cost-saving suggestions   |

**Example `/usage` response:**

```json
[
  {"date": "2025-06-20", "service": "Compute Engine", "usage_amount": 5.2},
  {"date": "2025-06-20", "service": "Cloud Run", "usage_amount": 1.3}
]
```

---

## 📈 How it works

1. **Provisioning**: Terraform scripts create all GCP resources in one command.
2. **Data Collection**: Usage/cost metrics are ingested into BigQuery (by GCP billing export or simulated loader).
3. **Analytics**: FastAPI endpoints query BigQuery, aggregate results, and return clean JSON.
4. **Recommendations**: Detects idle resources (e.g., VMs with zero usage for 30+ days) for easy cost reduction.

---

## 👤 About the Author

Built by [Arman Shirzad](armanshirzad.guru)
Software Engineer
M.Sc. Artificial Intelligence student at Brandenburg Technical University

[See my full CV →](./ARMAN%20SHIRZAD%20CV.pdf)

---

## 📝 License

MIT License (see [LICENSE](LICENSE))

---

## 🙌 Contributions & Feedback

Open to PRs, issues, and collaboration!
Feel free to [contact me](mailto:armanshirzad1998@gmail.com) for support or suggestions.

---

> *This project is intended for technical demonstrations, learning, and interview portfolios.
> It runs entirely in the Google Cloud free tier, with no proprietary or confidential data.*


