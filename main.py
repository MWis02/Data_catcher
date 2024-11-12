import psutil
from datetime import datetime

def server_info():

    physical_cores = psutil.cpu_count(logical=False) # Physical cores
    cores = psutil.cpu_count(logical=True) # Logical cores
    cpu_clk = psutil.cpu_freq() # CPU Frequency
    #cpu_temp = psutil.sensors_temperatures() # CPU Temperature

    ram_capacity = psutil.virtual_memory().total # RAM Capacity

    disc_capacity = psutil.disk_usage('/').total # Disk Capacity
    disc_usage = psutil.disk_usage('/').used # Disk Usage

    net_if_addrs = psutil.net_if_addrs() # Network Interfaces
    connected_devices = len(net_if_addrs) # Number of connected devices

    #th_bandwidth = psutil.net_if_addrs()

    print("Physical cores:", physical_cores)
    #print("CPU Temperature:", cpu_temp)
    print("Logical cores:", cores)
    print("CPU Frequency:", cpu_clk.max)
    print("RAM Capacity:", ram_capacity)
    print("Disk Capacity:", disc_capacity)
    print("Disk Usage:", disc_usage)
    print("Network Interfaces:", connected_devices)
    #print("Ethernet Bandwidth:", eth_bandwidth)



def server_status():

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = psutil.cpu_percent(interval=1)

    ram_total = psutil.virtual_memory().total
    ram_used = psutil.virtual_memory().used
    ram_usage = ram_used/ram_total*100

    disc_capacity = psutil.disk_usage('/').total
    disc_free = psutil.disk_usage('/').free
    disc_usage = 100 - (disc_free/disc_capacity*100)



    print("Current Time:", current_time)
    print("CPU Usage:", cpu_usage)
    print("RAM Total:", ram_total)
    print("RAM Used:", ram_used)
    print("RAM Usage:", ram_usage)
    print("Disk Capacity:", disc_capacity)
    print("Disk Free:", disc_free)
    print("Disk Usage:", disc_usage)


#def data_base():

if __name__ == '__main__':
    server_info()
    server_status()
    #data_base()