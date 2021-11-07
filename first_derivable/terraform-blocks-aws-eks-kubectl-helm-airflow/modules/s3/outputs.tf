output "s3_bucket_id" {
    value = aws_s3_bucket.bucket.id
}
output "s3_bucket_arn" {
    value = aws_s3_bucket.bucket.arn
}
output "s3_bucket_domain_name" {
    value = aws_s3_bucket.bucket.bucket_domain_name
}
output "s3_hosted_zone_id" {
    value = aws_s3_bucket.bucket.hosted_zone_id
}
output "s3_bucket_region" {
    value = aws_s3_bucket.bucket.region
}


output "s3_raw_bucket_id" {
    value = aws_s3_bucket.bucket_raw.id
}
output "s3_raw_bucket_arn" {
    value = aws_s3_bucket.bucket_raw.arn
}
output "s3_raw_bucket_domain_name" {
    value = aws_s3_bucket.bucket_raw.bucket_domain_name
}
output "s3_raw_hosted_zone_id" {
    value = aws_s3_bucket.bucket_raw.hosted_zone_id
}
output "s3_raw_bucket_region" {
    value = aws_s3_bucket.bucket_raw.region
}


output "s3_staging_bucket_id" {
    value = aws_s3_bucket.bucket_staging.id
}
output "s3_staging_bucket_arn" {
    value = aws_s3_bucket.bucket_staging.arn
}
output "s3_staging_bucket_domain_name" {
    value = aws_s3_bucket.bucket_staging.bucket_domain_name
}
output "s3_staging_hosted_zone_id" {
    value = aws_s3_bucket.bucket_staging.hosted_zone_id
}
output "s3_staging_bucket_region" {
    value = aws_s3_bucket.bucket_staging.region
}