variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
  default     = "demo-cloud-id"
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
  default     = "demo-folder-id"
}

variable "zone" {
  description = "Yandex Cloud availability zone"
  type        = string
  default     = "ru-central1-a"
}

variable "bucket_name" {
  description = "S3 bucket for Data Lake"
  type        = string
  default     = "smart-campus-data-lake"
}

variable "ssh_public_key" {
  description = "SSH public key for VM access"
  type        = string
  default     = "ssh-rsa AAAA_DEMO_KEY smart-campus"
}
