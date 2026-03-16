# Python Dict Comprehensions (Powerful & Concise)

1. Basic key-value mapping:
   ```python
   squares_dict = {x: x**2 for x in range(10)}
   # {0: 0, 1: 1, 2: 4, 3: 9, ..., 9: 81}
   ```
2.Filter and transform:Python
```
prices = {'apple': 0.5, 'banana': 0.3, 'cherry': 1.0}
expensive = {fruit: price for fruit, price in prices.items() if price > 0.4}
# {'apple': 0.5, 'cherry': 1.0}
```
3.Invert dict (keys to values):Python
```
inverted = {v: k for k, v in prices.items()}
# {0.5: 'apple', 0.3: 'banana', 1.0: 'cherry'}
```
4.With condition:Python
```
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_only = {k: v for k, v in data.items() if v % 2 == 0}
# {'b': 2, 'd': 4}
```
