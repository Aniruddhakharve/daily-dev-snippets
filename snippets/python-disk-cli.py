import shutil
import sys

threshold = int(sys.argv[1])

total, used, free = shutil.disk_usage("/")
usage = (used / total) * 100

if usage > threshold:
    print(f"⚠️ Disk usage high: {usage:.2f}%")
else:
    print(f"✅ Disk usage normal: {usage:.2f}%")
