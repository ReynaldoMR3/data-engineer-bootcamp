output "rds_hostname" {
  description = "RDS instance hostname"
  value       = aws_db_instance.rds-instance.address
}

output "rds_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.rds-instance.endpoint
}

output "rds_port" {
  description = "RDS instance port"
  value       = aws_db_instance.rds-instance.port
}

output "rds_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.rds-instance.username
  sensitive   = true
}

output "rds_security_group" {
  description = "rds security group name"
  value = aws_security_group.rds_sg.name
}

output "rds_instance_id" {
  value = aws_db_instance.rds-instance.id
}