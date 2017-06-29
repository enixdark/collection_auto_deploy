provider "aws" {
  region = "us-east-1"
}



resource "aws_db_instance" "example" {
  engine            = "mysql"
  allocated_storage = 10
  instance_class    = "db.t2.micro"
  name              = "example_database"
  username          = "${var.db_username}"
  password          = "${var.db_password}"
}