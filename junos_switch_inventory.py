from __future__ import print_function
from netmiko import ConnectHandler
from datetime import datetime
from jnpr.junos import Device

import os
import sys
import time
import select
import paramiko
import re
datestring = datetime.strftime(datetime.now(),'%Y%m%d%H%M%S')
os.chdir(r'C:\PROD\InfraRS\JunOS_inventory')
fd = open(r'junos-switch-ineventory-'+datestring+'.xml','w') 
old_stdout = sys.stdout   
sys.stdout = fd 
platform = 'juniper'
username = 'cisco'
password = 'cisco'
secret = ' '
verbose = False


ip_add_file = open(r'C:\DEV\INVENTORY\junos_switch.txt','r')

for host in ip_add_file:
    host = host.strip()
    device_conn = ConnectHandler( device_type=platform, ip=host, username=username, password=password, secret = secret, verbose=verbose)
	
    output = device_conn.send_command('show configuration | display xml | match host-name')
    print(output)

    output = device_conn.send_command('show chassis hardware | display xml | no-more')
    print(output)
    print("=========================================================================================")


fd.close()
