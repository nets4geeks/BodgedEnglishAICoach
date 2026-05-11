
import yaml
import logging
import sys
import os

from pathlib import Path

import utl
import t
import q
import w

def get(path,info=False):
   
    if info:
        logging.basicConfig(
           format='%(levelname)s:%(module)s:%(funcName)s():: %(message)s',
           level=logging.INFO
        )
    else:
        logging.basicConfig(
           format='%(levelname)s:%(module)s:%(funcName)s():: %(message)s',
        )

    logging.info("getting config file from "+path )
    with open(path, 'r') as file:
       config = yaml.safe_load(file)

    config['rez'] = config['data']+"/rez"


    return config


def vars(name,config):
    config['name'] = name
    config['path'] = config['rez']+"/"+config['name']
    config['questionsFile'] = config['path']+"/questions.json"
    config['dialogsFile'] = config['path']+"/dialogs.json"
    config['textFile'] = config['path']+"/text.json"
    config['wordsFile'] = config['path']+"/words.json"


# first time init folder & read source file
def init(path, name, config):
    
    vars(name, config)
    config['initFile'] = path

    logging.info("preparing folder "+config['path'] )
    utl.prepareFolder(config['path'])
    logging.info("getting src text from "+config['initFile'] )
    config['initText'] = utl.readFile(config['initFile'])


def load(name, config):

    vars(name, config)

    logging.info("loads data from "+config['path'] )
    t.load(config)
    q.load(config)
    w.load(config)

