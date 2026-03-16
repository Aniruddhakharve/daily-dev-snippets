# Advanced Bash Loops & Functions

1. While loop with counter:
   ```bash
   count=1
   while [ $count -le 5 ]; do
       echo "Iteration $count"
       ((count++))
   done
   ```
2.Until loop (opposite of while):Bash
```
num=10
until [ $num -eq 0 ]; do
    echo "Countdown: $num"
    ((num--))
done
```
3.Function with parameters & return:Bash
```
add_numbers() {
    local sum=$(( $1 + $2 ))
    echo "Sum: $sum"
    return $sum  # optional return value
}
add_numbers 5 7
echo "Returned: $?"
```
4.For loop over array:Bash
```
fruits=("apple" "banana" "cherry")
for fruit in "${fruits[@]}"; do
    echo "I like $fruit"
done
```
