#!/usr/bin/env python
import os
os.system("nmcli radio wifi off")
os.system("sudo macchanger -r eth0 ") # put your network card name instead of eth0
os.system("nmcli radio wifi on")
