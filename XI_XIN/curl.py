import os
import sys


## подсеть на какую меняется IP

network_to = "172.16.77."



## подсеть с какой меняется IP 


network_into = "192.168.1."
os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F{network_into}{sys.argv[1]}%3A8032%2Fweb%2Fnetwork.html&-ipaddr={network_to}{sys.argv[2]}&-netmask=255.255.255.0&-gateway={network_to}1&-dhcp=off&-dnsstat=0&-fdnsip={network_to}1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --max-time 2 --user admin:admin http://{network_into}{sys.argv[1]}:8032/web/cgi-bin/hi3510/param.cgi")

#os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F192.168.1.{line}%2Fweb%2Fnetwork.html&-ipaddr={network_to}{not_XM}&-netmask=255.255.254.0&-gateway={network_to}1&-dhcp=off&-dnsstat=0&-fdnsip={network_to}1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --max-time 3 --user admin:admin http://192.168.1.{line}/web/cgi-bin/hi3510/param.cgi")

