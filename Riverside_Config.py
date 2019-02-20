#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler


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

cisco_riv202 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.202',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

cisco_riv203 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.203',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}
for cisco_access_riv in (cisco_riv200, cisco_riv201, cisco_riv202, cisco_riv203,):
    net_connect = ConnectHandler(**cisco_access_riv)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
    write = net_connect.send_command("write mem")
    print(net_connect.find_prompt())
    print(output)
    print(write)

net_connect.disconnect()