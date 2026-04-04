
### Content
```python
file = "app.log"

with open(file, "r") as f:
    for line in f:
        if "ERROR" in line or "WARNING" in line:
            print(line.strip())
