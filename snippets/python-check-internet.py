
```python
# 🌐 Check Internet Connection in Python

import socket

def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if check_internet():
        print("✅ Internet is working")
    else:
        print("❌ No internet connection")
      ```
