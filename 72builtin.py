import os
files = os.popen("dir *.py")
for file in files:
    print(file)