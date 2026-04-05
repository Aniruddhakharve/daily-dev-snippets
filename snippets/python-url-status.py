
### Content
```python
import requests
import sys

url = sys.argv[1]

res = requests.get(url)
print(f"Status Code: {res.status_code}")
