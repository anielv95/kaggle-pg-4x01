resource "aws_key_pair" "my_key_pair" {
  key_name   = "my-key-pair"                   # Name for your key pair
  public_key = file("/gh/.ssh/key-pari-4.pub") # Path to your public key file
}


resource "aws_instance" "web" {
  ami           = var.official_debian_ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.my_key_pair.key_name

  tags = {
    Name = var.instance_type
  }
}

resource "aws_vpc_security_group_ingress_rule" "example" {
  security_group_id = var.security_group_id

  cidr_ipv4   = var.public_ip
  from_port   = 22
  ip_protocol = "tcp"
  to_port     = 22
}

resource "aws_vpc_security_group_ingress_rule" "jupyterlab-rule" {
  security_group_id = var.security_group_id

  cidr_ipv4   = var.public_ip
  from_port   = 8888
  ip_protocol = "tcp"
  to_port     = 8888
}
