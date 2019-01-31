#!/usr/bin/env python

from netmiko import ConnectHandler

cisco_riv202 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.202',
    'username': 'username',
    'password': 'password',
    'secret': 'secret',
}

net_connect = ConnectHandler(**cisco_riv202)
output = net_connect.send_command ('show vlan brief')
print(output)
