
### Content
```python
import os
import sys

file = sys.argv[1]

if os.path.exists(file):
    print("✅ File exists")
else:
    print("❌ File not found")
