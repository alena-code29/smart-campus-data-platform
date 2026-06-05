resource "yandex_compute_instance" "data_platform_vm" {
  name        = "smart-campus-data-platform-vm"
  platform_id = "standard-v3"
  zone        = var.zone

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = "fd8vmcue7aajpmeo39kk"
      size     = 30
      type     = "network-hdd"
    }
  }

  network_interface {
    subnet_id          = yandex_vpc_subnet.platform_subnet.id
    nat                = true
    security_group_ids = [yandex_vpc_security_group.platform_sg.id]
  }

  metadata = {
    ssh-keys = "ubuntu:${var.ssh_public_key}"
    user-data = <<EOF
#cloud-config
packages:
  - docker.io
  - docker-compose
runcmd:
  - systemctl enable docker
  - systemctl start docker
EOF
  }

  labels = local.labels
}
