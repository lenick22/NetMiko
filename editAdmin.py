#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from netmiko import Netmiko

cisco_riv200 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.200',
    'username': 'joes87',
    'password': 'Andrea;02$',
    'secret': 'b00nesw1ne',
}

cisco_riv201 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.201',
    'username': 'joes87',
    'password': 'Andrea;02$',
    'secret': 'b00nesw1ne',
}

cisco_riv202 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.202',
    'username': 'joes87',
    'password': 'Andrea;02$',
    'secret': 'b00nesw1ne',
}

cisco_riv203 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.203',
    'username': 'joes87',
    'password': 'Andrea;02$',
    'secret': 'b00nesw1ne',
}

for cisco_access_riv in (cisco_riv200, cisco_riv201, cisco_riv202, cisco_riv203):
    net_connect = Netmiko(**cisco_access_riv)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
print(output)

net_connect.disconnect()


