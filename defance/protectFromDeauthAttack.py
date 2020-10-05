import os
from scapy.all import *

wlan = raw_input("please specify the name of the interface you wish to use for Deauth attack detection: ")
numOfDeauth = 0
#here we will create a function that finds the number of deauth packets that have been sent to our network:
def DeauthPktCollector(pkt):
    #first we check to see if there is a payload to be transfered in the pkt we have collected.
    #Next, pkt type 0 on subtype 12 is deauth pkt, which means if the packet we have collected is in did type 0 on 12 we have obtained a deauth pkt.
    if(pkt.haslayer(Dot11FCS) & pkt.type == 0 & pkt.subtype == 0xc):
        numOfDeauth+=1
    if(numOfDeauth > 100): #if the number of deauth pkts we have collected is larger then 100 then our network is probably under attack.
        print("the program has detected over 100 packets of death. your network is probably under attack!!")


sniff(iface=wlan , prn = DeauthPktCollector)
