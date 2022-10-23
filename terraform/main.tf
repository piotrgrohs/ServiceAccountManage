locals {
  serviceAccounts = var.serviceAccounts
}


### variable.tf 

variable "serviceAccounts" {
  type = list(any)
}

## output.tf

output "serviceAccounts" {
  value = local.serviceAccounts
}