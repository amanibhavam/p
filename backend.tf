terraform {
  backend "remote" {
    organization = "katt"

    workspaces {
      name = "p"
    }
  }
}
