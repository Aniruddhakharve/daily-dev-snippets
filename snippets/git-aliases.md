# Git Aliases & Shortcuts

Save time with these global aliases:

1. Quick commit:
   ```bash
   git config --global alias.cm 'commit -m'
   ```
 Usage: git cm "Fix typo"

 git config --global alias.st 'status -sb'

 git reset --soft HEAD~1

 Add more daily! Day 1 basics.
text


4. Commit to new branch: `add-git-aliases-md`
5. PR title: "Add git-aliases.md with useful shortcuts"
6. Description: "Basic git aliases for faster workflow."
7. Create PR → Merge.

**PR 3: Add Python quick utils file**
1. New file: `snippets/python/quick-utils.py`
2. Paste:

```python
# Quick Python Utils - Day 1

def reverse_string(s: str) -> str:
    """Reverse a string efficiently."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (ignore case/spaces)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example
print(reverse_string("shark"))  # krahs
print(is_palindrome("A man a plan a canal Panama"))  # True
```

4. Quick log pretty:
   ```bash
   git config --global alias.lg "log --oneline --decorate --graph --all"
   ```
