resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_name
  location   = var.region
}

resource "google_bigquery_table" "usage" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = var.table_name
  time_partitioning {
    type  = "DAY"
    field = "timestamp"
  }
  schema = file("${path.module}/schema.json")
}

output "table_id" {
  value = google_bigquery_table.usage.id
}
