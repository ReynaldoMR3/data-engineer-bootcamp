# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
  access_key = "<key>"
  secret_key = "<key>"
}


# # How to create or provision a resource, example:
# resource "<provider>_<resource_type>" "name" {
#   config options ...
#   key = "value"
#   key2 = "another value"
# }


# resource "aws_instance" "my_first_ec2" {
#   ami =  "ami-00399ec92321828f5"    #  "copy the ami that is on the aws frontend of the resource"
#   instance_type = "t2.micro"
# }

# then we can use terraform destroy to destroy the resources
# Another way to destroy a resource is commenting the code or just delete it from the file
# read the documentation for the provider in terraform to get code examples

# resource "aws_vpc" "my_first_vpc" {
#   cidr_block = "10.0.0.0/16"

#   tags = {
#     Name = "production" #name needs to be written exactly Name, name doesn't work
#   }
# }

# resource "aws_subnet" "main" {
#   vpc_id     = aws_vpc.my_first_vpc.id # we use the name from the vpc, we reference the resource defined in the code usign the <resource>.<name>.id
#   cidr_block = "10.0.1.0/24"

#   tags = {
#     Name = "prod_subnet"
#   }
# }

# The code doesnt need to be written in order, i can create a resource after another and still reference the resource
# Remember to always look to the documentation, not everytime this rules applies, 

# Do not touch the terraform.tfstate this file is like a log and has all the information related to the resources created