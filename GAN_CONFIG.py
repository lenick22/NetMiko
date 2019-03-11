#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import os
from netmiko import ConnectHandler

#This configuration updates the switches in GAN

GANSW05 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.155',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW06 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.156',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW07 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.157',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW08 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.158',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW09 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.159',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW10 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.160',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW11 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.161',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW12 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.162',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW13 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.163',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW14 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.164',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW15 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.165',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW16 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.166',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW17 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.167',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW18 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.168',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW19 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.169',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}

GANSW20 = {
    'device_type': 'cisco_ios',
    'ip': '10.4.255.170',
    'username': os.environ.get('USER_NAME'),
    'password': os.environ.get('PASS'),
    'secret': os.environ.get('ENABLE'),
}




for GAN_DEVICES in (GANSW05, GANSW06, GANSW07, GANSW08, GANSW10, GANSW11, GANSW12, GANSW14, GANSW15, GANSW16, GANSW18, GANSW19, GANSW20,):
    net_connect = ConnectHandler(**GAN_DEVICES)
    net_connect.enable()  #get user past the enable
    output = net_connect.send_config_from_file('GAN_ISE_CONFIG')
    write = net_connect.send_command("write mem")
    print(net_connect.find_prompt()) #Prints out all the routers listed above
    print(output) #prints the output from the command vlan100
    print(write)


net_connect.disconnect()