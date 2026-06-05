resource "yandex_iam_service_account" "data_lake_sa" {
  name        = "smart-campus-data-lake-sa"
  description = "Service account for Smart Campus Data Lake"
}

resource "yandex_resourcemanager_folder_iam_member" "storage_editor" {
  folder_id = var.folder_id
  role      = "storage.editor"
  member    = "serviceAccount:${yandex_iam_service_account.data_lake_sa.id}"
}

resource "yandex_storage_bucket" "data_lake" {
  bucket    = var.bucket_name
  folder_id = var.folder_id

  labels = local.labels
}
