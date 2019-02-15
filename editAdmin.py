#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from netmiko import Netmiko
import os

cisco_riv200 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.200',
    'username': 'USER_NAME',
    'password': 'PASS',
    'secret': 'ENABLE',
}

cisco_riv201 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.201',
    'username': 'USER_NAME',
    'password': 'PASS',
    'secret': 'ENABLE',
}

cisco_riv202 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.202',
    'username': 'USER_NAME',
    'password': 'PASS',
    'secret': 'ENABLE',
}

cisco_riv203 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.203',
    'username': 'USER_NAME',
    'password': 'PASS',
    'secret': 'ENABLE',
}

for cisco_access_riv in (cisco_riv200, cisco_riv201, cisco_riv202, cisco_riv203):
    net_connect = Netmiko(**cisco_access_riv)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
print((cisco_riv200)output)

net_connect.disconnect()


