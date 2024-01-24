variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my_creds.json"
}


variable "project" {
  description = "Project"
  default     = "terra_demo_431941"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-west-04"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "test_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "terra-test-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}