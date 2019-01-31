#!/usr/bin/env python

from netmiko import ConnectHandler

cisco_riv202 = {
    'device_type': 'cisco_ios',
    'ip': '10.214.128.202',
    'username': 'joes87',
    'password': 'Andrea;02$',
    'secret': 'b00nesw1ne',
}

net_connect = ConnectHandler(**cisco_riv202)
output = net_connect.send_command ('show vlan brief')
print(output)
