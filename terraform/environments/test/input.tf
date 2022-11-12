# Azure GUIDS
variable "subscription_id" { default =  "7de72e36-dc87-4e3f-aa67-6dacbc9993c6"}
variable "client_id" {default="d6fb68d2-3677-431e-8b99-772992a4a821"}
variable "client_secret" {default="5Mo8Q~83oQ-lehxbH5PdEzuJrHOp~GdINJAiea2y"}
variable "tenant_id" {default="f958e84a-92b8-439f-a62d-4f45996b6d07"}

# Resource Group/Location
variable "location" { default="South Central US"}
variable "resource_group" { default="Azuredevops"}
variable "application_type" {default="sinlq3-udacity-project3"}

# Network
variable virtual_network_name {default = "sinlq3-vn"}
variable address_prefix_test { default =   "10.5.1.0/24"}
variable address_space {default=["10.5.0.0/16"]}


variable admin_username {default = "sinlq3"}
variable admin_password {default=""}

variable vm_name {default = "sinlq3-vm"}

variable resource_group_name {default = "Azuredevops"}
