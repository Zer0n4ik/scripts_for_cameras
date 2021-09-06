import os


import time

ips = []
#f = open('ipsHI.txt', 'r').read().splitlines()
#print(f)\
#for ip in f:
 #   ips.append(ip)
 #   print(ip)
#print(f)
#ips = []
#ips.append(ip)
b = 4
aaa = "192.168.1."
#print(ips)
for i in range(6,250):
    b = b +1
    print(i)
    print(aaa + str(b)) 

#    print(i)
    os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F192.168.1.{i}%2Fweb%2Fnetwork.html&-ipaddr=192.168.1.{i}&-netmask=255.255.255.0&-gateway=192.168.1.1&-dhcp=off&-dnsstat=0&-fdnsip=192.168.1.1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://192.168.1.{i}/web/cgi-bin/hi3510/param.cgi")
   # print(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F{i}%2Fweb%2Fnetwork.html&-ipaddr={i}&-netmask=255.255.255.0&-gateway=192.168.1.1&-dhcp=off&-dnsstat=0&-fdnsip=192.168.1.1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://{i}/web/cgi-bin/hi3510/param.cgi")
