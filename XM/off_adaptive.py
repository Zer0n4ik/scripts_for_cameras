from dvrip import DVRIPCam
import subprocess
import os
#with open




network_to = '172.16.77.'


# подсеть с которой убирать adaptive
network_into = '192.168.1.'





not_XM = 151

for line in range(23,254):
    
    print(line)
    print(f"подключаюсь к камере 172.16.77.{line}")
    try:
        cam = DVRIPCam(f"192.168.216.{line}", user='admin', password='')

        cam.login()




        
        net = cam.get_info("NetWork.IPAdaptive") 
        print(net)
        cam.set_info("NetWork.IPAdaptive", { "IPAdaptive": False } )     

### вывод данных о СЕТИ на камере XM
        print(net)
    except Exception:
        print("EXCEPTION")
        pass
