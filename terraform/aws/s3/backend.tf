terraform {
  backend "s3" {
    bucket = "terraform-bucket-s3-sample"
    key = "global/s3/terraform.tfstate"
    region = "us-east-1"
    encrypt=true
  }
}
