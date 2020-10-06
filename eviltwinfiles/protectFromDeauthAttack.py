import os
from scapy.all import *

numOfDeauth = 0
#here we will create a function that finds the number of deauth packets that have been sent to our network:
def DeauthPktCollector(pkt):
    global numOfDeauth
    #first we check to see if there is a payload to be transfered in the pkt we have collected.
    #Next, pkt type 0 on subtype 12 is deauth pkt, which means if the packet we have collected is in did type 0 on 12 we have obtained a deauth pkt.
    if(pkt.haslayer(Dot11FCS)):
	if(pkt.type == 0):
		if(pkt.subtype == 12):
			numOfDeauth+=1
		        #print(numOfDeauth)
    if(numOfDeauth > 100): #if the number of deauth pkts we have collected is larger then 100 then our network is probably under attack.
        print("the program has detected over 100 packets of death. your network is probably under attack!!")



wlan = raw_input("please specify the name of the interface you wish to use for Deauth attack detection: ")
sniff(iface=wlan , prn = DeauthPktCollector)
