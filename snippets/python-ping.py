
### Content
```python
import os

host = "8.8.8.8"
response = os.system(f"ping -c 1 {host}")

if response == 0:
    print("✅ Host reachable")
else:
    print("❌ Host unreachable")
