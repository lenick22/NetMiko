#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler



GDMGW = {
    'device_type': 'cisco_ios',
    'ip': '10.76.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
    'port': 23,
}




net_connect = ConnectHandler(**GDMGW)
net_connect.enable()
output = net_connect.send_config_from_file('vlan1000.txt')
print(net_connect.find_prompt())  # Prints out all the routers listed above
print(output)  # prints the output from the command vlan100


net_connect.disconnect()