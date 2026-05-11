

import uuid
import json
import logging

import utl
import tts
import inf
import llm



def getInitWords(config):
    wordsToProcess = utl.getWords(config['initText'])
    lst = []
    for wordToProcess in wordsToProcess:
        logging.info('processing word: '+ wordToProcess)
        config['currentWord'] = wordToProcess
        word = llm.ask(config['wordTemplate'], config)
        word['id'] = uuid.uuid4().hex[:16] 
        lst.append(word)
    return {'words': lst }


def save(words, config):
    logging.info("saving words" )
    utl.saveFile(config['wordsFile'],  json.dumps(words, indent=4))


def load(config):
    logging.info("reading words file" )
    config['words'] = json.loads(utl.readFile(config['wordsFile']))['words']


def notEmpty(config):
    if len(config['words']) == 0:
         return False
    return True
    


def show(n, typ, config):
    if typ == 'q':
        inf.show("Word question", n, config['words'][n]['id'], config['words'][n]['explanation'], config['textTemplate'])
    if typ == 'a':
        s = config['words'][n]['word']+": "+config['words'][n]['explanation']+"\n\n"+config['words'][n]['example1']+"\n"+config['words'][n]['example2']+"\n\n( "+config['words'][n]['translation']+" )"
        inf.show("Word answer", n, config['words'][n]['id'], s, config['textTemplate'])
    if config['gab'] :
        say(n, typ, config)


def say(n, typ, config):
    if typ == 'q':
        tts.say(config['words'][n]['id']+'q', config['words'][n]['explanation'], config)
    if typ == 'a':
        s = config['words'][n]['word']+": "+config['words'][n]['explanation']+"\n\n"+config['words'][n]['example1']+"\n"+config['words'][n]['example2']
        tts.say(config['words'][n]['id']+'a', s, config)

def findex(config):
    return len(config['words'])-1
