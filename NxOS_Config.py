#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from netmiko import Netmiko

cisco_nxos = {
    'device_type': 'cisco_nxos',
    'ip': '10.214.128.6',
    'username': 'admin',
    'password': '1qaz2wsx;',
    'secret': 'b00nesw1ne',
}

net_connect = Netmiko(**cisco_nxos)
net_connect.enable()
output = net_connect.send_config_from_file('NexusConfig')
print(output)

net_connect.disconnect()

