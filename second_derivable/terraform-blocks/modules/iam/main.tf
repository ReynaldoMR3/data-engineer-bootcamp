resource "aws_iam_user" "s3_reader" {
  name = var.iam_s3_name
}

resource "aws_iam_access_key" "s3_reader" {
  user = aws_iam_user.s3_reader.name
}

resource "aws_iam_user_policy" "s3_reader_ro" {
  name = var.s3_reader_ro_name
  user = aws_iam_user.s3_reader.name

  policy = var.s3_policy
}