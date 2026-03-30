# 🔄 Undo Last Git Commit (Safely)

## 🧠 Scenario
You made a commit but want to undo it without losing changes.

---

## ✅ Keep Changes (Uncommit but keep files)
```bash
git reset --soft HEAD~1

## Remove Commit + Changes (Danger)
git reset --hard HEAD~1

## Undo Commit but Keep Changes Unstaged
git reset --mixed HEAD~1
```
