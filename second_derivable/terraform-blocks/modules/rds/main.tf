resource "aws_security_group" "rds_sg_second" {
  name = var.sg_second_name

  description = "RDS servers (using terraform)"
  vpc_id = var.vpc_id_rds_second

  ingress {
      from_port = var.db_port_second
      to_port = var.db_port_second
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }

  egress = {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_subnet_group" "db_subnet_second" {
    name = var.db_subnet_name
    subnet_ids = var.subnets_rds_second
}

resource "aws_db_instance" "postgres-instance" {
    allocated_storage      = var.allocated_storage_second
    storage_type           = "gp2"
    engine                 = var.db_engine_second
    engine_version         = var.engine_version_second
    instance_class         = var.instance_type_second
    name                   = var.database_name_second
    username               = var.db_username_second
    password               = var.db_password_second
    skip_final_snapshot    = true
    db_subnet_group_name   = aws_db_subnet_group.db_subnet_second.name
    publicly_accessible    = var.publicly_accessible_second
    vpc_security_group_ids = [
        aws_security_group.rds_sg_second.id
    ] 
}
