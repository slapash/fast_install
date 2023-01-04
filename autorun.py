import os 

path = os.getcwd()
filenames = os.listdir(path)

for elem in filenames:
    if elem[:2] != "._" and elem != "autorun.py":
        os.startfile(os.path.join(path, elem))