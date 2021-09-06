from dvrip import DVRIPCam
import subprocess
import os
#with open




### network_to 
##  FOR XIXIN подсеть на которую сменить ФОРМАТ '192.168.1.'
network_to = '172.16.76.'

# подсеть с которой будет меняться ип
network_into = "192.168.1."

### FOR XIXIN
octet_1 = format(172, 'x').upper()
octet_2 = format(16, 'x').upper()
octet_3 = format(76, 'x').upper()
if len(octet_1) == 1:
    octet_1 = "0" + octet_1 
elif len(octet_1) >= 3:
    print("ошибка IP адерса: " ,octet_1)
else:
    pass


if len(octet_2) == 1:
    octet_2 = "0" + octet_2
elif len(octet_2 >= 3:
    print("ошибка IP адерса: " ,octet_2)
else:
    pass


if len(octet_3) == 1:
    octet_3 = "0" + octet_3 
elif len(octet_3) >= 3:
    print("ошибка IP адерса: " ,octet_3)
else:
    pass



print(octet_3, octet_2,octet_1)


####  count  с какого ипа будут настраиватся камеры XM.
count = 21

####  not_XM камеры HIXIN ипы которые будут выдаваться им по очереди

not_XM = 151

###  указать подсеть с какой менять IP 
network_into = "192.168.1."


for line in range(11,250):
    
    print(line)
    print(f"подключаюсь к камере {network_into}{line}")
    try:
        cam = DVRIPCam(f"{network_into}{line}", user='admin', password='')

        cam.login()



### преобразование из DEC в HEX ип камеры со значения count +=1
        count3 = format(count, 'x').upper()
        print("COUNT3", count3)
        


### вывод данных о СЕТИ на камере XM
        net = cam.get_info("NetWork.NetCommon") 
        print(net)
        
## смена ип адреса в HEX формате

        cam.set_info("NetWork.NetCommon.HostIP", f"0x{count3}{octet_3}{octet_2}{octet_1}")
        
### смена NETMASK на XM камере 
        cam.set_info("NetWork.NetCommon.Submask", "0x00FFFFFF")
        print(100*"-")
        print(f"success connect to {network_into}{line}")
        
       #count += 1
        cam.close()
        count += 1
    except:

#### смена IP адреса на не XM камерах (XIXIN)


        responses = subprocess.Popen(["ping","-c","2",f"{network_into}{line}"]).wait()
        print("NOT XM", not_XM)
        if responses == 0:
            try:
                
                print("--"*100)
                os.system(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F{network_into}{line}%2Fweb%2Fnetwork.html&-ipaddr={network_to}{not_XM}&-netmask=255.255.254.0&-gateway={network_to}1&-dhcp=off&-dnsstat=0&-fdnsip={network_to}1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --max-time 2 --user admin:admin http://{network_into}{line}/web/cgi-bin/hi3510/param.cgi")
                not_XM +=1
            #    print(f"curl -d 'cmd=setnetattr&cururl=http%3A%2F%2F192.168.1.{line}%2Fweb%2Fnetwork.html&-ipaddr=172.16.76.{not_XM}&-netmask=255.255.254.0&-gateway=172.16.76.1&-dhcp=off&-dnsstat=0&-fdnsip=172.16.76.1&-sdnsip=%22%22&cmd=setrtspauth&-rtsp_aenable=0&cmd=setrtspport&-rtspport=554&cmd=setrtmpattr&-rtmpport=1935&cmd=sethttpport&-httpport=8032' --user admin:admin http://192.168.1.{line}/web/cgi-bin/hi3510/param.cgi")
            except Exception:
                print("CONNECTION REFUSE")
        else:
            print(f"NO CONNECTION TO CAM {network_into}{line}")

