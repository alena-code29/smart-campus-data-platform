resource "yandex_vpc_network" "platform_network" {
  name = "smart-campus-network"
}

resource "yandex_vpc_subnet" "platform_subnet" {
  name           = "smart-campus-subnet"
  zone           = var.zone
  network_id     = yandex_vpc_network.platform_network.id
  v4_cidr_blocks = ["10.10.0.0/24"]
}

resource "yandex_vpc_security_group" "platform_sg" {
  name       = "smart-campus-security-group"
  network_id = yandex_vpc_network.platform_network.id

  ingress {
    protocol       = "TCP"
    description    = "SSH"
    v4_cidr_blocks = ["0.0.0.0/0"]
    port           = 22
  }

  ingress {
    protocol       = "TCP"
    description    = "Web UIs"
    v4_cidr_blocks = ["0.0.0.0/0"]
    from_port      = 3000
    to_port        = 9001
  }

  egress {
    protocol       = "ANY"
    description    = "Outbound traffic"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }
}
