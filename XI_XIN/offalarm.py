import os


import time


network_into = "192.168.1."
#print(ips)
for i in range(3,254):
    print(i)

#    print(i)
    #os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F192.168.1.{i}%2Fweb%2Fnetwork.html&-ipaddr=192.168.1.{i}&-netmask=255.255.255.0&-gateway=192.168.1.1&-dhcp=off&-dnsstat=0&-fdnsip=192.168.1.1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://192.168.1.{i}/web/cgi-bin/hi3510/param.cgi")
    os.system(f"curl -d 'cmd=setsmdattr&cururl=http%3A%2F%2F{network_into}{i}%3A8032%2Fweb%2Falarmsmd.html&-smd_enable=0&cmd=setsmdex&-smd_rect=0&-smd_gthresh=25&cmd=setmdalarm&-aname=type&-switch=on' --max-time 3 --user admin:admin http://{network_into}{i}:8032/web/cgi-bin/hi3510/param.cgi")
