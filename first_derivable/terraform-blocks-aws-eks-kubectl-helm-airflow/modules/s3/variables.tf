variable "bucket_prefix" {
  type = string
}

variable "bucket_raw_prefix" {
  type = string
}

variable "bucket_staging_prefix" {
  type = string
}

variable "iam_user" {
  type = string
}

variable "acl" {
  type = string
  default = "False"
}

variable "versioning" {
  type = bool
}

variable "subnet_s3" {
  description = "Networking subnets"
}

variable "vpc_id_s3" {
  description = "VPC id"
}
