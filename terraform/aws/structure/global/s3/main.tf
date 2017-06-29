provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "terraform_state" {
  bucket = "terraform-bucket-s3-stage"
  acl    = "public-read"
  
  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}

