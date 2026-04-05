
### Content
```python
import time
import requests

start = time.time()
requests.get("https://google.com")
end = time.time()

print(f"Latency: {(end - start)*1000:.2f} ms")
