resource "yandex_mdb_kafka_cluster" "smart_campus_kafka" {
  name        = "smart-campus-kafka"
  environment = "PRESTABLE"
  network_id  = yandex_vpc_network.platform_network.id
  subnet_ids  = [yandex_vpc_subnet.platform_subnet.id]

  config {
    version          = "3.5"
    zones            = [var.zone]
    brokers_count    = 1
    assign_public_ip = true

    kafka {
      resources {
        resource_preset_id = "s2.micro"
        disk_type_id       = "network-hdd"
        disk_size          = 10
      }
    }
  }
}
