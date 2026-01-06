resource "aws_key_pair" "my_key_pair" {
  key_name   = "my-key-pair"                   # Name for your key pair
  public_key = file("/gh/.ssh/key-pari-4.pub") # Path to your public key file
}


resource "aws_instance" "web" {
  ami           = "resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-minimal-kernel-default-x86_64"
  instance_type = "t2.micro"
  key_name      = aws_key_pair.my_key_pair.key_name

  tags = {
    Name = "t2micro"
  }
}

