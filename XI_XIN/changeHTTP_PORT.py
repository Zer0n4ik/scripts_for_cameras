import os


import time


network_into = "192.168.1."
for i in range(6,250):
    print(i)

#    print(i)
    os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F{network_into}{i}%2Fweb%2Fnetwork.html&-ipaddr={network_into}{i}&-netmask=255.255.255.0&-gateway={network_into}1&-dhcp=off&-dnsstat=0&-fdnsip={network_into}1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://{network_into}{i}/web/cgi-bin/hi3510/param.cgi")
   # print(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F{i}%2Fweb%2Fnetwork.html&-ipaddr={i}&-netmask=255.255.255.0&-gateway=192.168.1.1&-dhcp=off&-dnsstat=0&-fdnsip=192.168.1.1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://{i}/web/cgi-bin/hi3510/param.cgi")
