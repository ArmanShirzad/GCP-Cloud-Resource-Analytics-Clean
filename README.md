# Cloud Resource Analytics Dashboard

This project provisions GCP resources using Terraform and exposes a FastAPI
service to query usage and cost data stored in BigQuery.

## Prerequisites
- [Terraform](https://www.terraform.io/) installed locally
- A Google Cloud account with billing enabled

## Setup
1. **Configure Terraform variables** in `terraform/terraform.tfvars`:
   ```hcl
   project_id  = "<your-gcp-project>"
   api_image   = "gcr.io/<your-project>/analytics-api:latest"
   ```
2. **Deploy infrastructure**:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```
3. **Build & push API image**:
   ```bash
   docker build -t gcr.io/<your-project>/analytics-api:latest .
   docker push gcr.io/<your-project>/analytics-api:latest
   terraform apply -target=module.api
   ```
4. **Call the API** using the Cloud Run URL output from Terraform.

## Development
- Python code lives in `app/`.
- Terraform modules live in `terraform/modules/`.
- CI checks syntax and Terraform formatting.
