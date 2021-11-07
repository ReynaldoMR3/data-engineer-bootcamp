output "region" {
  description = "AWS region"
  value       = var.region
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = var.cluster_name
}

output "efs" {
  value = module.eks.efs
}


output "s3_bucket_id" {
    value = module.s3.s3_bucket_id
}
output "s3_bucket_arn" {
    value = module.s3.s3_bucket_arn
}
output "s3_bucket_domain_name" {
    value = module.s3.s3_bucket_domain_name
}
output "s3_hosted_zone_id" {
    value = module.s3.s3_hosted_zone_id
}
output "s3_bucket_region" {
    value = module.s3.s3_bucket_region
}


output "s3_raw_bucket_id" {
    value = module.s3.s3_raw_bucket_id
}
output "s3_raw_bucket_arn" {
    value = module.s3.s3_raw_bucket_arn
}
output "s3_raw_bucket_domain_name" {
    value = module.s3.s3_raw_bucket_domain_name
}
output "s3_raw_hosted_zone_id" {
    value = module.s3.s3_raw_hosted_zone_id
}
output "s3_raw_bucket_region" {
    value = module.s3.s3_raw_bucket_region
}


output "s3_staging_bucket_id" {
    value = module.s3.s3_staging_bucket_id
}
output "s3_staging_bucket_arn" {
    value = module.s3.s3_staging_bucket_arn
}
output "s3_staging_bucket_domain_name" {
    value = module.s3.s3_staging_bucket_domain_name
}
output "s3_staging_hosted_zone_id" {
    value = module.s3.s3_staging_hosted_zone_id
}
output "s3_staging_bucket_region" {
    value = module.s3.s3_staging_bucket_region
}