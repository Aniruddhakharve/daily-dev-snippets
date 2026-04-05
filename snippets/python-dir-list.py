import os
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "."

for file in os.listdir(path):
    print(file)
