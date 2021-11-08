output "vpc_id" {
  value = aws_vpc.vpc.id
}

output "vpc_cidr_block" {
  value = var.vpc_cidr
}

output "cidr_block" {
  value = aws_vpc.vpc.cidr_block
}

output "public_subnets_route_table_id" {
  value = aws_route_table.public.id
}

output "public_subnets_ids" {
  value = aws_subnet.public_subnet.id
}

output "private_subnets_route_table_id" {
  value = aws_route_table.private.id
}

output "private_subnets_ids" {
  value = aws_subnet.private_subnet.*.id
}

output "nat_gw_ids" {
  value = aws_nat_gateway.nat.id
}

output "internet_gateway_id" {
  value = aws_internet_gateway.igw.id
}

output "availability_zone" {
  value = var.availability_zone
}

output "aws_security_group_id" {
  value = aws_security_group.default.id
}

output "aws_subnet_public_subnet"{
  value = aws_subnet.public_subnet
}