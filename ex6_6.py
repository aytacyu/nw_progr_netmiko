#!/usr/bin/env python
"""
Optional, connect to three networking devices one after the other. Use send_command() to execute a
show command on each of these devices. Print this output to the screen.
"""
from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from getpass import getpass

def output_printer(output):
    print()
    print('-' * 80)
    print(output)
    print('-' * 80)
    print()



cisco1 = {
    'host': '192.168.10.130',
    'username': 'cisco',
    'password': "cisco",
    'device_type': 'cisco_ios',
    'command': 'show ip int brief',
}

cisco2 = {
    'host': '192.168.10.131',
    'username': 'cisco',
    'password': "cisco",
    'device_type': 'cisco_ios',
    'command': 'show ip int brief',
}
for device in (cisco1, cisco2):
    command = device.pop('command')
    net_connect = Netmiko(**device)
    output = net_connect.send_command(command)
    output_printer(output)
