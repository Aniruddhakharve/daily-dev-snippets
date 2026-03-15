# Python List Comprehensions (Fast & Clean)

1. Basic square numbers:
   ```python
   squares = [x**2 for x in range(10)]
   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```
 2. Filter even numbers:Python
    ```
    evens = [x for x in range(20) if x % 2 == 0]
     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    ```
 3. Nested comprehension (matrix flatten):Python
    ```
    matrix = [[1, 2], [3, 4]]
    flat = [num for row in matrix for num in row]
    # [1, 2, 3, 4]
    ```
4. With condition and transformation:Python
   ```
   words = ["hello", "world", "python"]
   upper_short = [w.upper() for w in words if len(w) > 4]
    # ['HELLO', 'WORLD', 'PYTHON']
   ```
