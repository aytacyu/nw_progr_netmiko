#!/usr/bin/env python
"""Establish a connection to the network device and print out the device's prompt."""


#import logging
from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from getpass import getpass

"""
logging.basicConfig(filename="log.txt",level=logging.DEBUG)
logger=logging.getLogger("netmiko")"""


try:
    host = raw_input("Enter host ip with dotted format: ")
except NameError:
    host = input("Enter host ip with dotted format: ")
username=getpass("Enter Username:")
password=getpass("Enter Password:")
"""
host="192.168.10.130"
username="cisco"
password="cisco"
"""
device = {
    "host":host,
    "username":username,
    "password":password,
    "device_type":"cisco_ios",
    "secret":"cisco"
}
net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()

