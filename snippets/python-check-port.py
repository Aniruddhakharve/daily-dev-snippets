
### Content
```python
import socket

host = "127.0.0.1"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((host, port))

if result == 0:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed")

sock.close()
