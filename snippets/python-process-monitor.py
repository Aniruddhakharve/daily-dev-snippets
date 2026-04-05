import psutil

for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    print(proc.info)
