import psutil
import pymysql
from datetime import datetime
import time


def server_info():

    physical_cores = psutil.cpu_count(logical=False) # Physical cores
    cores = psutil.cpu_count(logical=True) # Logical cores
    cpu_freq_max = psutil.cpu_freq() # CPU Frequency
    #cpu_temp = psutil.sensors_temperatures() # CPU Temperature

    ram_capacity = psutil.virtual_memory().total # RAM Capacity

    disc_capacity = psutil.disk_usage('/').total # Disk Capacity
    disc_usage = psutil.disk_usage('/').used # Disk Usage

    net_if_addrs = psutil.net_if_addrs() # Network Interfaces
    connected_devices = len(net_if_addrs) # Number of connected devices

    #th_bandwidth = psutil.net_if_addrs()

    boot_time = datetime.fromtimestamp(psutil.boot_time()) # Boot time of machine

    print("------------------------------------------------------")
    print("-server_info")
    print("------------------------------------------------------")
    print("Physical cores:", physical_cores)
    #print("CPU Temperature:", cpu_temp)
    print("Logical cores:", cores)
    print("CPU Frequency:", cpu_freq_max.max)
    print("RAM Capacity:", ram_capacity)
    print("Disk Capacity:", disc_capacity)
    print("Disk Usage:", disc_usage)
    print("Network Interfaces:", connected_devices)
    #print("Ethernet Bandwidth:", eth_bandwidth)
    print("Boot_time:", boot_time)

    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="linuxobserver-bookit.l.aivencloud.com",
        password="AVNS_qaEEOa7DolLX6bPDtjQ",
        read_timeout=timeout,
        port=22474,
        user="avnadmin",
        write_timeout=timeout,
    )

    try:
        cursor = connection.cursor()
        # cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
        insert = (f"INSERT INTO `linuxobserver`.`SERVER_spec` (`physical_cores`,`logical_cores`,`max_cpu_clock`,"
                  f"`alert_temp_cpu`,`ram_capacity`,`max_disc_capacity`,`max_IO_num`,`server_start_date`) VALUES "
                  f"({physical_cores}, {cores}, {cpu_freq_max.max}, 105 ,{ram_capacity}, {disc_usage}, 0, {boot_time})")
        cursor.execute(insert)
        # cursor.execute("SELECT * FROM mytest")
        # print(cursor.fetchall())
    finally:
        connection.close()

def server_status():

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu_usage = round(psutil.cpu_percent(interval=1), 3)
    cpu_freq = round(psutil.cpu_freq().current, 0)

    ram_total = round(psutil.virtual_memory().total/1024/1024, 0)
    ram_used = round(psutil.virtual_memory().used/1024/1024, 0)
    ram_available = round(psutil.virtual_memory().available/1024/1024, 0)

    disc_capacity = round(psutil.disk_usage('/').total/1024/1024, 2)
    disc_free = round(psutil.disk_usage('/').free/1024/1024, 2)
    disc_usage = round(100 - (disc_free/disc_capacity*100), 2) # to na backendzie

    io_disc_start = psutil.disk_io_counters()
    io_net_start = psutil.net_io_counters()
    time.sleep(10)
    io_disc_end = psutil.disk_io_counters()
    io_net_end = psutil.net_io_counters()

    #a to juz pewnie na backendzie, zeby nie przeciazac bazy danych
    read_count_diff = io_disc_end.read_count - io_disc_start.read_count
    write_count_diff = io_disc_end.write_count - io_disc_start.write_count
    read_bytes_diff = io_disc_end.read_bytes - io_disc_start.read_bytes
    write_bytes_diff = io_disc_end.write_bytes - io_disc_start.write_bytes

    net_packets_sent = io_net_end.packets_sent - io_net_start.packets_sent
    net_packets_recv = io_net_end.packets_recv - io_net_start.packets_recv

    print("\n ------------------------------------------------------")
    print("server_status")
    print("------------------------------------------------------")
    print("Current Time:", current_time)
    print("CPU Usage:", cpu_usage, "%")
    print("CPU Frequency:", cpu_freq)
    print("RAM Total:", ram_total, "MB")
    print("RAM available", ram_available, "MB")
    print("RAM Used:", ram_used, "MB")
    print("RAM Usage:", round((ram_used / ram_total)*100,2), "%") #to backend
    print("Disk Capacity:", disc_capacity)
    print("Disk Free:", disc_free)
    print("Disk Usage:", disc_usage)
    print("IO read count:", read_count_diff)
    print("IO write count:", write_count_diff)




if __name__ == '__main__':
    server_info()
    server_status()
