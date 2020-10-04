# 💀Evil twin attack💀
# Created by: 
### 🙊Avihu Oshri
### 🙉Daniel Ventura 
### 🙈Din Avrunin

For educational Purposes only! we take no responsibility/liability of any kind from the use of this program.
Dont use this program on any network that isn't yours and use at your own risk.

Explaination:
For our final project in Ariel University we have created a hacking tool based on the "evil-twin attack" concept.
We choose which network we wish to impersonate to and become a third unknown party where all the traffic between clients and that network goes through us, we have complete control and can decide whether to steal information quietly without any of the sides knowing about it, or redirecting the parties to where we want, or just disconnecting them from the internet.


### Hardware:
💻 Laptop <br>
📡 Tenda Wireless N150 High-Power USB Adapter / TP LINK Wn722n wifi adapter / any other WIFI adapter that suportt Monitor mode 
   and packet injecting <br>
⚡ Operation system: 🐲 Kali linux


### Software:
Virtual box <br>
Python <br>
Scapy <br>
Dnsmasq <br>
multiprocessing <br>
sys <br>
rpcbind <br>
hostapd <br>
Apache server <br>
airmon-ng <br>
airodump - only for bonus handshake capture!! <br>
aircrack - only for bonus handshake capture!! <br>
bc <br>


## special problems:
we had issues with configuring TP LINK WN722N VERSION3 interface to monitor mode so we used a special set of commands to fix this issue int file MonitorMode.sh in the file section 



How is it done:
We first search for a network, we use airodump to find details about that network like BSSID,ESSID,Channel and such.
Then, we create an access point with the same credentials as the network that we want to attack.
We send DAuth message to disconnect any users connected to that network (their system try to automatically reconnect but instead it reconnects to our network).
We open a window on the client's side asking for the wifi password again.
We then redirect all traffic from the clients to the Network.



test:

# First step :
  git clone https://github.com/Avihuoshri/EvilTwinAttack.git <br>
  move the files IntelLogo.png, index.php and victim_passwords.txt to the folder /var/www/html. <br>
  ### (copy all existing file in the original html directory to new html_copy directory)
# Second step :
  start terminal in root command and execute the next command:  python DeAuthAttack.py 
  enter commands in this order:
  wlan1,
  wlan1,
  then detect the BSSID of your desired network and copy + paste it. <br>
  after a few seconds you should see planty of packets, press ctrl C at any time. <br>
  detect the client mac address copy + paste it 
  decide how many packets you want to send (2 should be enough
  now wait until the specific user u decided on disconnects from the internet. <br>
  
  ### victim connects to the real password protected AP:
  <img src="gif files/real_AP_connection.gif" width="600" height="350" >
 
  ### victim disconnected from real AP and then connects to fake unprotected AP:
  <img src="gif files/victim_reconnect_to_fa_ap.gif" width="600" height="350" >


  
# Third step : 
start a new terminal and execute the command ./fake-ap-start.sh
enter SSL password: "123456" to connect to websites like google , Facebook etc. (install SSL if neccessary)

<img src="gif files/fake_ap_creation.gif" width="600" height="350" >

# Fourth step - 
You can find the password file in /var/www/html/victim_password.txt path <br>
<img src="gif files/victim_passowrd.gif" width="600" height="350" >



