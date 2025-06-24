resource "google_compute_instance" "default" {
  name         = "demo-vm"
  machine_type = "e2-micro"
  zone         = "${var.region}-a"
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }
  network_interface {
    network = "default"
    access_config {}
  }
  scheduling {
    preemptible       = true
    automatic_restart = false
  }
}
