#module "iam" {
#source = "./modules/iam"
#}

module "s3" {
    source = "./modules/s3"

    vpc_id_s3 = module.networking.vpc_id
    subnet_s3 = module.networking.private_subnets_ids

    bucket_prefix = var.bucket_prefix
    acl = var.acl
    versioning = var.versioning  
}

