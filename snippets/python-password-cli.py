
### Content
```python
import random
import string

chars = string.ascii_letters + string.digits
print("".join(random.choice(chars) for _ in range(10)))
