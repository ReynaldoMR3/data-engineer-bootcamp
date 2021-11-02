variable "sg_second_name" {
    description = "Name of the rds security group"
    type = string
}

variable "vpc_id_rds_second" {
    description = "VPC id"
}

variable "db_port_second" {
    description = "Database port"
    type = number
}

variable "db_subnet_name" {
    description = "Database subnet name"
    type = string
}

variable "subnets_rds_second" {
    description = "Private subnet where the rds instance is going to be placed"
}

variable "allocated_storage_second" {
    description = "Space in disk for the database, stay in the range 5-10 to stay in free tier"
    type = number
}

variable "db_engine_second" {
    description = "Database instance type"
    type = string
}


variable "engine_version_second" {
    description = "Engine version"
    type = string
}

variable "instance_type_second" {
    description = "Type for the rds instance, set db.t3.micro to stay in the free tier"
    type = string
}

variable "database_name_second" {
  description = "Name for the rds database"
  type = string
}

variable "db_username_second" {
  description = "Username credentials for root user"
}

variable "db_password_second" {
    description = "Password credentials for root user"
}

variable "publicly_accessible_second" {
  description = "Variable that set the instance to be accessible publicly"
}