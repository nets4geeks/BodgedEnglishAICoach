
import uuid
import json
import logging

import utl
import tts
import inf
import llm
import re


def getCrams(config):

    text = config['initText'].replace("[", "").replace("]", "")
    sentences = re.split(r'(?<=[.!?]) +', text.replace ("\n"," "))
    cramsToProcess = [" ".join(sentences[i:i+3]) for i in range(0, len(sentences), 3)]

    lst = []
    i=0;
    for cramToProcess in cramsToProcess:
        if cramToProcess != "":
            logging.info('processing cram: '+ str(i))
            cram = {}
            cram['text'] = re.sub(r'([!.?])', r'\1\n', cramToProcess)

            config['translateText'] = cramToProcess
            output = llm.ask2(config['translateTemplate'], config)
            cram['translate'] = re.sub(r'([!.?])', r'\1\n', output)
            cram['id'] = uuid.uuid4().hex[:16] 
            lst.append(cram)
          
            i=i+1

    return {'crams': lst }


def save(crams, config):
    logging.info("saving crams" )
    utl.saveFile(config['cramsFile'],  json.dumps(crams, indent=4))


def load(config):
    logging.info("reading crams file" )
    config['crams'] = json.loads(utl.readFile(config['cramsFile']))['crams']


def notEmpty(config):
    if len(config['crams']) == 0:
         return False
    return True


def findex(config):
    return len(config['crams'])-1


def show(n, config):
    inf.show("Cram", n, config['crams'][n]['id'], config['crams'][n]['text']+"\n"+config['crams'][n]['translate'], config['textTemplate'])
    if config['gab'] :
        say(n, config)


def say(n, config):
    tts.say(config['crams'][n]['id'], config['crams'][n]['text'], config)

