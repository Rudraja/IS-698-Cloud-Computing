# Define the AWS provider
provider "aws" {
  region = "us-east-1"  # Change if needed
}

# Create an EC2 instance
resource "aws_instance" "Lab6" {
  ami           = "ami-08b5b3a93ed654d19"  # AMI ID from extracted details
  instance_type = "t2.micro"
  key_name      = "Lab6"  # Replace with your actual key pair name

  # Attach the network interface (private IP will be auto-assigned)
  network_interface {
    network_interface_id = aws_network_interface.lab6_nic.id
    device_index         = 0
  }

  tags = {
    Name = "Lab6"  # Instance Name
  }
}

# Create a network interface with auto-assigned private IP
resource "aws_network_interface" "lab6_nic" {
  subnet_id = "subnet-02d41d703752f879d"  # Subnet ID from extracted details
}

# Output instance details (Public IP and DNS)
output "public_ip" {
  value = aws_instance.Lab6.public_ip
}

output "public_dns" {
  value = aws_instance.Lab6.public_dns
}

