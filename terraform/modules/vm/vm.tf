resource "azurerm_network_interface" "" {
  name                = "${var.virtual_network_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group_name}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = ""
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = "${var.vm_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group_name}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  network_interface_ids = []
  admin_password = "${var.admin_password}"
  admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "file('~/.ssh/id_rsa.pub')"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
