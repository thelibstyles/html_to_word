import os

with os.scandir('test_files') as entries:
    for entry in entries:
        print(entry.name)



