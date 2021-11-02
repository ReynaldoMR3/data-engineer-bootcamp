output "postgres_hostname" {
  description = "RDS instance hostname"
  value       = aws_db_instance.postgres-instance.address
}

output "postgres_endpoint" {
  description = "RDS instance endpoint"
  value       = aws_db_instance.postgres-instance.endpoint
}

output "postgres_port" {
  description = "RDS instance port"
  value       = aws_db_instance.postgres-instance.port
}

output "postgres_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.postgres-instance.username
  sensitive   = true
}