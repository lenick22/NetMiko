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

GDAGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.50.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('TELENABLE'),
}

GIFGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.78.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('TELENABLE'),
}

GKEGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.92.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GKFGW = {
    'device_type': 'cisco_ios',
    'ip': '10.94.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GKGGW = {
    'device_type': 'cisco_ios',
    'ip': '10.97.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GIEGW = {
    'device_type': 'cisco_ios',
    'ip': '10.74.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}



for cisco_access_riv in (cisco_riv200, cisco_riv201,):
    net_connect = Netmiko(**cisco_access_riv)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
print(output)
print("Riverside Access Switch Update complete")

for REMOTE_SITES in (GDAGW, GIFGW, GKEGW, GKFGW, GKGGW, GIEGW,):
    net_connect = Netmiko(**REMOTE_SITES)
    net_connect.enable()
    output = net_connect.send_config_from_file('vlan1000.txt')
print(output)
print("Remote Site Configuration Complete")

net_connect.disconnect()