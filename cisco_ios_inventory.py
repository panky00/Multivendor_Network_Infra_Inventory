from __future__ import print_function
from netmiko import ConnectHandler
from datetime import datetime

import os
import sys
import time
import select
import paramiko
import re
datestring = datetime.strftime(datetime.now(),'%Y-%m-%d-%H-%M')
os.chdir(r'C:\DEV\RAW_DATA')
fd = open(r'cisco-ios-inventory.txt','w') 
old_stdout = sys.stdout   
sys.stdout = fd 
platform = 'cisco_ios'
username = 'cisco'
password = 'cisco'


ip_add_file = open(r'C:\DEV\INVENTORY\cisco_ios_router.txt','r')

for host in ip_add_file:
    host = host.strip()
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('terminal length 0')
           
    output = device.send_command('show configuration | i hostname')
    print(output)
    output = device.send_command('show inventory')
    print(output)


fd.close()
