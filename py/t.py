
# a text document

import uuid
import json
import logging

import utl
import tts
import inf
import llm

def save(config):
    logging.info("saving text file" )
    text = config['initText'].replace("[", "").replace("]", "")
    new = { 'id': uuid.uuid4().hex[:16], 'text': text }
    utl.saveFile(config['textFile'], json.dumps(new, indent=4))


def load(config):
    logging.info("reading text file" )
    config['text'] = json.loads(utl.readFile(config['textFile']))

def show(config):
    inf.show("Text", config['name'], config['text']['id'], config['text']['text'], config['textTemplate'])
    if config['gab'] :
        say(config)


def say(config):
    tts.say(config['text']['id'], config['text']['text'], config)


def check(text,config):
    config['checkText'] = text
    output = llm.ask2(config['checkTemplate'], config)
    inf.show("Recommendation", config['model'], "temp: "+str(config['temperature']), output, config['textTemplate'])
#    if config['gab'] :
#        tts.tmp(output,config)

def translate(text,config):
    config['translateText'] = text
    output = llm.ask2(config['translateTemplate'], config)
    inf.show("Translation", config['model'], "temp: "+str(config['temperature']), output.replace(". ", ".\n"), config['textTemplate'])


def translateText(config):
    return translate(config['text']['text'],config)

def clarify(text,config):
    config['clarifyText'] = text
    output = llm.ask2(config['clarifyTemplate'], config)
    inf.show("Clarification", config['model'], "temp: "+str(config['temperature']), output, config['textTemplate'])
    if config['gab'] :
        tts.tmp(output,config)


def query(text,config):
    config['queryText'] = text
    output = llm.ask2(config['queryTemplate'], config)
    inf.show("Query", config['model'], "temp: "+str(config['temperature']), output, config['textTemplate'])
    if config['gab'] :
        tts.tmp(output,config)


def printLessons(config):
    arr = utl.getFolder(config['rez'])
    sn = ""
    for index, value in enumerate(arr):
        sn = sn + "["+str(index)+"] "+str(value)+"   "

    inf.show("Lessons", "", str(len(arr)), sn, config['textTemplate'])

    return arr


