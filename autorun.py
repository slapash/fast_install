import os 
import json


path = os.getcwd()
config_file = os.path.join(path, "config.json")
config_file_open = open(config_file)
filenames = json.load(config_file_open)


for elem in filenames['logiciels']:
    os.startfile(os.path.join(path, elem))