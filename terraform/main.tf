module "bq" {
  source       = "./modules/bq_module"
  dataset_name = var.dataset_name
  table_name   = var.table_name
}

module "api" {
  source    = "./modules/api_module"
  region    = var.region
  project_id = var.project_id
  image     = var.api_image
}

module "vm" {
  source    = "./modules/vm_core"
  project_id = var.project_id
  region    = var.region
}
