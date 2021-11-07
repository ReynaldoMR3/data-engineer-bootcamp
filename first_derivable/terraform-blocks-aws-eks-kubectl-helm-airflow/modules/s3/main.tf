resource "aws_s3_bucket" "bucket" {
  bucket_prefix = var.bucket_prefix

  versioning {
    enabled = var.versioning
  }

  tags = {
    Name = "airflow_rds_second_derivable"
  }
}

resource "aws_s3_bucket" "bucket_staging" {
  bucket_prefix = var.bucket_staging_prefix

  versioning {
    enabled = var.versioning
  }

  tags = {
    Name = "third_derivable"
  }
}

resource "aws_s3_bucket" "bucket_raw" {
  bucket_prefix = var.bucket_raw_prefix

  versioning {
    enabled = var.versioning
  }

  tags = {
    Name = "third_derivable"
  }
}