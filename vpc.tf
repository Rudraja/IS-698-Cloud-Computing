resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"  # The VPC CIDR block
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"  # Public subnet CIDR block
  map_public_ip_on_launch = true
  availability_zone        = "us-east-1a"  # Availability zone for public subnet
}

resource "aws_subnet" "private_subnet" {
  vpc_id           = aws_vpc.my_vpc.id
  cidr_block       = "10.0.2.0/24"  # Private subnet CIDR block
  availability_zone = "us-east-1b"  # Availability zone for private subnet
}
