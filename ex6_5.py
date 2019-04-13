#!/usr/bin/env python
"""
Optional, use send_command() in conjunction with ntc-templates to execute a show command. Have
TextFSM automatically convert this show command output to structured data.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

def output_printer(output):
    print()
    print('-' * 80)
    print(output)
    print('-' * 80)
    print()

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
}

command = 'show ip int brief'
net_connect = Netmiko(**device)
output = net_connect.send_command(command, use_textfsm=True)
output_printer(output)
