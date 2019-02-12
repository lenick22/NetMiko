#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import Netmiko


GDN = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.50.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('TELENABLE'),
}


net_connect = Netmiko(**GDN)
net_connect.enable()
output = net_connect.send_config_from_file('vlan1000.txt')
print(output)

net_connect.disconnect()