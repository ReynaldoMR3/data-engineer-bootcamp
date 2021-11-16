variable "iam_user" {
  type = string
  description = "name for the iam user"
}

variable "s3_bucket_arn" {
  description = "arn needed for the iam permissions"
}

variable "s3_raw_bucket_arn" {
  description = "arn needed for the iam permissions"
}

variable "s3_staging_bucket_arn" {
  description = "arn needed for the iam permissions"
}


variable "rds_instance" {
  description = "rds instance identifier"
}

variable "default_security_group" {
  description = "default security group defined in networking"
}