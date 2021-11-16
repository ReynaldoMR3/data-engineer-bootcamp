resource "aws_iam_policy" "buckets_policy" {
  name = "policyForBuckets"
   policy = data.aws_iam_policy_document.buckets_document.json
}


data "aws_iam_policy_document" "buckets_document" {
  statement {
    effect = "Allow"
    sid = "s3Import"
    actions= [
      "s3:ListBucket",
      "s3:GetObject",
      "s3:PutObject"
    ]
    resources = [
      var.s3_bucket_arn,
      var.s3_raw_bucket_arn,
      var.s3_staging_bucket_arn,
      "${var.s3_bucket_arn}/*",
      "${var.s3_raw_bucket_arn}/*",
      "${var.s3_staging_bucket_arn}/*"
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
  #groups = ["${var.default_security_group}"]
}



resource "aws_db_instance_role_association" "rds-role-attach" {
  db_instance_identifier = var.rds_instance
  feature_name           = "s3Import"
  role_arn               = aws_iam_role.rds_role.arn
}