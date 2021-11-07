resource "aws_iam_policy" "buckets_policy" {
  name = "policyForBuckets"
   policy = data.aws_iam_policy_document.buckets_document.json
}


data "aws_iam_policy_document" "buckets_document" {
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket"
    ]
    resources = [
      aws_s3_bucket.bucket.arn,
      aws_s3_bucket.bucket_raw.arn,
      aws_s3_bucket.bucket_staging.arn
    ]
  }
  statement {
    effect = "Allow"
    actions= [
      "s3:GetObject",
      "s3:PutObject"
    ]
    resources = [
      "${aws_s3_bucket.bucket.arn}/*",
      "${aws_s3_bucket.bucket_raw.arn}/*",
      "${aws_s3_bucket.bucket_staging.arn}/*"
    ]
  }
}

resource "aws_iam_user" "user" {
  name = var.iam_user
}

resource "aws_iam_role" "rds_role" {
  name = "rds-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17", 
  "Statement": [
    {
      "Effect": "Allow", 
      "Principal": {
      "Service": "rds.amazonaws.com"
      }, 
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy_attachment" "policy-attach" {
  name       = "policy-attachment"
  users      = [aws_iam_user.user.name]
  roles      = [aws_iam_role.rds_role.name]
  policy_arn = aws_iam_policy.buckets_policy.arn
}