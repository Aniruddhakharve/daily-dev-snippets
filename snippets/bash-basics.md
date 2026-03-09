# Bash Basics & Handy Commands

1. Create directory + cd into it:
   ```bash
   mkcd() { mkdir -p "$1" && cd "$1"; }
   ```
2. Find all TODO comments in code:
   ```
   grep -r "# TODO" .
   ```
1.Quick disk usage summary:Bash
```
du -sh * | sort -h
```
Day 1 essentials — more tomorrow!
text
```

