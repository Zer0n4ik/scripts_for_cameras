import os
import time


from dvrip import DVRIPCam


### синхронизация времени на 2х типах камер
# octet_1_3 подсеть с какой синхронизировать камеры 


octet_1_3 = "192.168.1."


for sync in range(3,254):


    try:
        cam = DVRIPCam(f'{octet_1_3}{sync}', user='admin', password='')
        cam.login()
        cam.set_time()
        cam.close()

    except Exception:
        try:
            a = time.strftime("%Y.%m.%d.%H.%M.%S")
            os.system(f"curl -u 'admin:admin' -d 'cmd=setservertime&-time={a}&-timezone=Europe%2FDublin&dstmode=&cmd=setntpattr&ntpenable=' http://{octet_1_3}{sync}:8032/web/cgi-bin/hi3510/param.cgi")
        except Exception:
            pass
        pass

