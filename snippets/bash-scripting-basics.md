```markdown
# Bash Scripting Basics

1. Simple hello script (save as hello.sh):
   ```bash
   #!/bin/bash
   echo "Hello, $1! Welcome to Bash scripting."
```
```
Run: chmod +x hello.sh && ./hello.sh Random
```
```
2. Check if file exists:Bash
if [ -f "config.txt" ]; then
    echo "File exists!"
else
    echo "File not found."
fi
```
```
3. Loop over files:Bash
for file in *.txt; do
    echo "Processing $file"
done
```
```
Function example:Bash
greet() {
    echo "Hi $1, have a great day!"
}
greet "Dev"
```
