#!/bin/sh

echo  "----------------------------\e[1;31m Stopping services \e[0m----------------------------"
service hostapd stop
echo  "hostapd - \e[1;31m STOPED \e[0m"
service apache2 stop
echo  "apache2 - \e[1;31m STOPED \e[0m"
service dnsmasq stop
echo  "dnsmasq - \e[1;31m STOPED \e[0m"
service rpcbind stop
echo  "rpcbind - \e[1;31m STOPED \e[0m"
killall dnsmasq
killall hostapd

