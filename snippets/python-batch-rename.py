
### Content
```python
import os

folder = "."

for count, filename in enumerate(os.listdir(folder)):
    new_name = f"file_{count}.txt"
    os.rename(filename, new_name)

print("✅ Files renamed")
