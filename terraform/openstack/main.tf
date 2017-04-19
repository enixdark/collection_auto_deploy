# Configure the OpenStack Provider
provider "openstack" {
  user_name   = "admin"
  tenant_name = "admin"
  password    = "631f96d4d24249ef"
  auth_url    = "http://10.1.0.10:5000/v2.0"
}

resource "openstack_blockstorage_volume_v1" "vol" {
  name = "vol"
  size = 1
}

resource "openstack_compute_instance_v2" "basic" {
  name            = "terraform_node"
  image_id        = "4c597d5a-91fb-4be1-a10a-e901d28578a7"
  flavor_id       = "2"
  key_pair        = "node1"
  security_groups = ["default"]

  metadata {
    this = "that"
  }

  network {
    name = "private_network"
  }

  volume {
    volume_id = "${openstack_blockstorage_volume_v1.vol.id}"
  }
}

