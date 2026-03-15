```markdown
# Productivity Tip: Smart .gitignore Usage

1. Global .gitignore (for all repos):
   ```bash
   git config --global core.excludesfile ~/.gitignore_global

  Then add to ~/.gitignore_global:

.DS_Store
*.log
Thumbs.db

2. Per-repo .gitignore patterns:text

# Python
__pycache__/
*.pyc

# Logs
*.log
logs/

# Temp
*.tmp
temp/
```
