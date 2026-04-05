
### Content
```python
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <name>")
else:
    print(f"Hello, {sys.argv[1]}!")
