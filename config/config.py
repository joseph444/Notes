import json
import os

def getConfig():
    path=os.getcwd()
    with open(path+"/config/config.json") as f:
        data=json.load(f)

    return data