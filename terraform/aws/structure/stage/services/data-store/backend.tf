terraform {
  backend "s3" {
    bucket = "terraform-bucket-s3-stage"
    key = "stage/data-stores/mysql/terraform.tfstate"
    region = "us-east-1"
    # encrypt=true
  }
}


