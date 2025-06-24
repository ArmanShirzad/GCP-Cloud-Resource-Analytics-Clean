variable "project_id" {
  description = "GCP project id"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "dataset_name" {
  description = "BigQuery dataset name"
  type        = string
  default     = "usage_data"
}

variable "table_name" {
  description = "BigQuery table name"
  type        = string
  default     = "resource_usage"
}

variable "api_image" {
  description = "Docker image for Cloud Run"
  type        = string
}
