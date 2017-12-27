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
fd = open(r'mrv-switch-interface.txt','w') 
old_stdout = sys.stdout   
sys.stdout = fd 
platform = 'mrv_optiswitch'
username = 'pankaj.sharma'
password = '1Ofnc8qOyb8WMzTIdm0ey5kp'


ip_add_file = open(r'C:\DEV\INVENTORY\mrvi.txt','r') 

for host in ip_add_file:
    host = host.strip()
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('enable')
           
    output = device.send_command('show port')
    print(output)


fd.close()
