import psutil

def server_info():
    physical_cores = psutil.cpu_count(logical=False)
    cores = psutil.cpu_count(logical=True)
    cpu_clk = psutil.cpu_freq()
    ram_capacity = psutil.virtual_memory().total
    disc_capacity = psutil.disk_usage('/').total
    disc_usage = psutil.disk_usage('/').used
    io_counters = psutil.net_io_counters()
    eth_bandwidth = psutil.net_if_addrs()

    print("Physical cores:", physical_cores)
    print("Logical cores:", cores)
    print("CPU Frequency:", cpu_clk.max)
    print("RAM Capacity:", ram_capacity)
    print("Disk Capacity:", disc_capacity)
    print("Disk Usage:", disc_usage)
    print("IO Counters:", io_counters)
    print("Ethernet Bandwidth:", eth_bandwidth)



#def server_status():

#def data_base():

if __name__ == '__main__':
    server_info()
    #server_status()
    #data_base()