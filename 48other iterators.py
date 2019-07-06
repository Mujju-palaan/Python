import os
files = os.popen('dir *.py')
fileit = iter(files)
for file in files:
    print(files)
####################
import os
files = os.popen('dir *.py')
fileit = iter(files)
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))
print(next(fileit))