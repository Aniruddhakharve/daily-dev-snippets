# Python Error Handling Best Practices

1. Basic try-except:
   ```python
   try:
       result = 10 / 0
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   ```
2.  Catch multiple exceptions:Python
    ```
    try:
    num = int(input("Enter a number: "))
    except (ValueError, TypeError) as e:
    print(f"Invalid input: {e}")
    ```
3. Finally block (always runs):Python
   ```
   try:
    file = open("data.txt")
   except FileNotFoundError:
    print("File not found!")
   finally:
    print("Cleanup done.")
  ``
4. Raise custom exception:Python
   ```
if age < 0:
    raise ValueError("Age cannot be negative!")
```
