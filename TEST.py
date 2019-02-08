#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import Netmiko


cisco_riv200 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.200',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

cisco_riv201 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.201',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}


for cisco_access_riv in (cisco_riv200, cisco_riv201,):
    net_connect = Netmiko(**cisco_access_riv)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
print(output)

net_connect.disconnect()