#!/usr/bin/env python
"""
Find a command on your device that has additional prompting. Use send_command_timing to send the
command down the SSH channel. Capture the output and handle the additional prompting.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

try:
    host = raw_input("Enter host to connect to: ")
except NameError:
    host = input("Enter host to connect to: ")

password = getpass()
device = {
    'host': host,
    'username': 'cisco',
    'password': password,
    'device_type': 'cisco_ios',
    "secret":"cisco"
}

command = "copy run start\n"

net_connect = Netmiko(**device)
net_connect.enable()
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
if 'Destination filename' in output:
    output += net_connect.send_command_timing('startup-config', strip_prompt=False, strip_command=False)
else:
    raise ValueError("Expected confirm message in output")

print()
print('-' * 80)
print(output)
print('-' * 80)
print()
