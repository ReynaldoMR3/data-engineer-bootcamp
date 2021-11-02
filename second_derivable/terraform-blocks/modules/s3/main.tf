resource "aws_s3_bucket" "csv_files" {
  bucket_prefix = var.bucket_prefix

  versioning {
    enabled = var.versioning
  }

  tags = {
    Name = "s3-second-derivable"
  }
}