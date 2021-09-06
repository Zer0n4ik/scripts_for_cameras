from dvrip import DVRIPCam
import sys



### FOR XM
octet_1 = format(172, 'x').upper()
octet_2 = format(16, 'x').upper()
octet_3 = format(76, 'x').upper()
count3 = format(171, 'x').upper()

host_ip = "192.168.216.29"

cam = DVRIPCam(host_ip, user="admin",password="")
if cam.login():
    net = cam.get_info("NetWork.NetCommon")
    print(net)
    #cam.set_info("NetWork.IPAdaptive", { "IPAdaptive": False } )
    cam.set_info("NetWork.NetCommon.HostIP", f"0x{count3}{octet_3}{octet_2}{octet_1}")
else:
    print("connection false (((")
