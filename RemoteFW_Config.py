#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler

GDAFW = {
    'device_type': 'cisco_ios',
    'ip': '10.50.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GKEFW = {
    'device_type': 'cisco_ios',
    'ip': '10.92.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GKGFW = {
    'device_type': 'cisco_ios',
    'ip': '10.97.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GIEFW = {
    'device_type': 'cisco_ios',
    'ip': '10.74.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GIHFW = {
    'device_type': 'cisco_ios',
    'ip': '10.84.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDLFW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.60.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJBFW = {
    'device_type': 'cisco_ios',
    'ip': '10.56.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJCFW = {
    'device_type': 'cisco_ios',
    'ip': '10.58.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDBFW = {
    'device_type': 'cisco_ios',
    'ip': '10.52.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDMFW = {
    'device_type': 'cisco_ios',
    'ip': '10.76.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GIIFW = {
    'device_type': 'cisco_ios',
    'ip': '10.90.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJAFW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.42.1.254',
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJEFW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.64.1.254',
    'username': os.environ.get('FWNAME'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJFFW = {
    'device_type': 'cisco_ios',
    'ip': '10.68.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDNFW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.80.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDOFW = {
    'device_type': 'cisco_io',
    'ip': '10.86.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDPFW = {
    'device_type': 'cisco_ios',
    'ip': '10.96.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GJHFW = {
    'device_type': 'cisco_ios',
    'ip': '10.98.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GDFFW = {
    'device_type': 'cisco_ios',
    'ip': '10.48.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GKFFW = {
    'device_type': 'cisco_ios_telnet',
    'ip': '10.94.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}

GIFFW = {
    'device_type': 'cisco_ios',
    'ip': '10.78.1.254',
    'username': os.environ.get('FWUSER'),
    'password': os.environ.get('FWPASS'),
    'secret': os.environ.get('FWPASS'),
}
for REMOTE_SITES in (GDAFW, GKEFW, GKGFW, GIEFW, GIHFW, GDLFW, GJBFW, GJCFW, GDBFW, GDMFW, GIIFW, GJAFW, GJEFW, GJFFW, GDNFW, GDOFW, GDPFW, GJHFW, GDFFW, GKFFW, GIFFW,):
    net_connect = ConnectHandler(**REMOTE_SITES)
    net_connect.enable()  #get user past the enable
    output = net_connect.send_config_from_file('NTP_Settings')
    write = net_connect.send_command("write mem")
    print(net_connect.find_prompt()) #Prints out all the routers listed above
    print(output) #prints the output from the command vlan100
    print(write)

net_connect.disconnect()