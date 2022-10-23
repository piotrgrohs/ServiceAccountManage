# Terraform use of JSON list

### Commands

```
# init
$ terraform init
# plan 
$ terraform plan -var-file=../serviceAccount.json

Changes to Outputs:
  + serviceAccounts = [
      + jsonencode(
            {
              + app         = "apple"
              + description = ""
              + id          = 0
              + project     = "project1"
            }
        ),
    ]