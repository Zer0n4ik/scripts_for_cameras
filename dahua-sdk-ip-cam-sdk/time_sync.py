from dahua_rpc import DahuaRpc



### Подсеть с которой синхронизировать камеры
network_into = "192.168.1."
for sync in range(3,254):
    try:
        dahua = DahuaRpc(host=f"{network_into}{sync}", username="admin", password="")
        dahua.login()
        print(dahua.current_time())
        dahua.set_time()
        print(dahua.current_time())
    except Exception:
        print("Exception")
        pass
