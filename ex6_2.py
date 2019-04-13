#!/usr/bin/env python
"""
Use send_command() to send a show command down the SSH channel. Retrieve the results and print the
results to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass


try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")


#host = "192.168.10.130"

password = getpass("Enter password: ")

device = {
    'host': host,
    'username': 'cisco',
    'password': password,
    'device_type': 'cisco_ios',
}
command = 'show ip int brief'
net_connect = Netmiko(**device)
output = net_connect.send_command(command)
print()
print('-' * 80)
print(output)
print('-' * 80)
print()
