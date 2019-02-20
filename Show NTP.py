#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler



GDAGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.50.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
}

GIFGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.78.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
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


GIHGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.84.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GIIGW = {
    'device_type': 'cisco_ios',
    'ip': '10.90.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GDLGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.60.1.1',
    'username': os.environ.get('NUSER'),
    'password': os.environ.get('NPASS'),
    'secret': os.environ.get('ENABLE'),
}

GJAGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.42.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
}

GJBGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.56.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
}

GJCGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.58.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
}

GJEGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.64.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GJFGW = {
    'device_type': 'cisco_ios',
    'ip': '10.68.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GDBGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.52.1.1',
    'password': os.environ.get('TELPASS'),
    'secret': os.environ.get('ENABLE'),
}


GDNGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.80.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GDOGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.86.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GDPGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.96.1.1',
    'username': 'joes87',
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}


GJHGW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.98.1.1',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

for REMOTE_SITES in (GDAGW, GIFGW, GKEGW, GKFGW, GKGGW, GIEGW, GIHGW, GIIGW, GDLGW, GJAGW, GJBGW, GJCGW, GJEGW, GJFGW, GDBGW, GDNGW, GDOGW, GDPGW, GJHGW,):
    net_connect = ConnectHandler(**REMOTE_SITES)
    net_connect.enable()
    show = net_connect.send_command("show version")
    print(net_connect.find_prompt()) #Prints out all the routers listed above
    print(show)


net_connect.disconnect()