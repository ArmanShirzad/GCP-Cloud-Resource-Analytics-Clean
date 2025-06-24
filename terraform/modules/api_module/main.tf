resource "google_service_account" "api_sa" {
  account_id   = "api-sa"
  display_name = "API service account"
}

resource "google_cloud_run_service" "api" {
  name     = "analytics-api"
  location = var.region

  template {
    spec {
      containers {
        image = var.image
      }
      service_account_name = google_service_account.api_sa.email
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service_iam_member" "invoker" {
  location        = google_cloud_run_service.api.location
  project         = var.project_id
  service         = google_cloud_run_service.api.name
  role            = "roles/run.invoker"
  member          = "allUsers"
}

output "url" {
  value = google_cloud_run_service.api.status[0].url
}

resource "google_project_iam_member" "api_sa_bigquery_jobuser" {
  project = var.project_id
  role    = "roles/bigquery.jobUser"
  member  = "serviceAccount:${google_service_account.api_sa.email}"
}

resource "google_project_iam_member" "api_sa_bigquery_dataviewer" {
  project = var.project_id
  role    = "roles/bigquery.dataViewer"
  member  = "serviceAccount:${google_service_account.api_sa.email}"
}
