output "bucket_name" {
  value = yandex_storage_bucket.data_lake.bucket
}

output "vm_name" {
  value = yandex_compute_instance.data_platform_vm.name
}

output "kafka_cluster_name" {
  value = yandex_mdb_kafka_cluster.smart_campus_kafka.name
}
