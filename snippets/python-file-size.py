
### Content
```python
import os

file = input("Enter file path: ")

if os.path.exists(file):
    size = os.path.getsize(file)
    print(f"Size: {size} bytes")
else:
    print("File not found")
