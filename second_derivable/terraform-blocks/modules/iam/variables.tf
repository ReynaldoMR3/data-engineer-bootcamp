variable "iam_s3_name" {
    description = "The name of the iam user for s3"
    type        = string
}

variable "s3_reader_ro_name" {
  description = "name of the policy"
  type        = string
}

variable "s3_policy" {
    description = "Policy to be used"
    type = string
}