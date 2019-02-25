#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from getpass import getpass

password = getpass()

rivsw_202 = {
    "host": "10.214.128.202",
    "username": 'USER',
    "password": 'PASSWORD',
    "secret": "ENABLE",
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**rivsw_202)
net_connect.enable()
cfg_commands = ['no username TESTADMIN privilege 15 password TESTtest123']
# send_config_set() will automatically enter/exit config mode
output = net_connect.send_config_set(cfg_commands)
print(output)

net_connect.disconnect()