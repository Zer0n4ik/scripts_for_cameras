from dahua_rpc import DahuaRpc

dahua = DahuaRpc(host="192.168.1.108" , username="admin",password="")

dahua.login()
#object_id = dahua.get_traffic_info() 
print(dahua.current_time())



### Change IP address on dahua Camera


params = {"name":"Network","table":{"DefaultInterface":"eth0","Domain":"dauha","Hostname":"IPC","eth0":{"DefaultGateway":"192.168.1.1","SubnetMask": "255.255.255.0","IPAddress":"192.168.1.108"}}}

dahua.set_config(params)
#dahua.set_time()
#print(object_id)
#print(dahua.current_time())
