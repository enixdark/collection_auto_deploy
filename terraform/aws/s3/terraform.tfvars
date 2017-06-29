terragrunt = {
  terraform {
    lock = {
      backend = "dynamodb"

      config {
        state_file_id = "global/s3"
      }
    }


    remote_state {
      encrypt = "true"
      bucket  = "terraform-bucket-s3-sample"
      key     = "global/s3/terraform.tfstate"
      region  = "us-east-1"
    }
  }
}