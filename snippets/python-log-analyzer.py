# 🔥 Simple Log Analyzer (Counts ERROR lines)

file = "app.log"

error_count = 0

with open(file, "r") as f:
    for line in f:
        if "ERROR" in line:
            error_count += 1

print(f"Total ERROR lines: {error_count}")
