
import yaml
import logging
import sys
import os
import glob
from pathlib import Path
import re



def readFile(path):
    logging.info("reading file from "+path )
    with open(path, "r") as f:
        output =  f.read()
    return output

def saveFile(path,data):
    logging.info("saving file to "+path )

    with open(path, "w", encoding="utf-8") as f:
       f.write(data)
       f.close()

def prepareFolder(path):
    logging.info("creating folder "+path )
    Path(path).mkdir(exist_ok=True)


def getFolder(fld):
    path = Path(fld)
    arr=[]
    for item in path.iterdir():
        
        arr.append(item.name)

    return sorted(arr)     

def getWords(text):
    return re.findall(r'\[(.*?)\]', text)



