
### Content
```python
import psutil

mem = psutil.virtual_memory()
print(f"Total: {mem.total // (2**30)} GB")
print(f"Used: {mem.used // (2**30)} GB")
print(f"Free: {mem.available // (2**30)} GB")
