
import uuid
import json
import logging

import utl
import tts
import inf
import llm

def init(config):
    config['context'] = []
    config['currentResponse'] =  llm.chat(config, "hello")
    config['currentResponseNum'] =  0



def get(config):
    return config['currentResponse']


def nxt (config,msg):
    config['currentResponse'] = llm.chat(config, msg)
    config['currentResponseNum'] = config['currentResponseNum']+1


def say (config):
    tts.tmp(config['currentResponse'],config)

def show(config):
    inf.show("Dialog with", config['model'], str(config['currentResponseNum']), config['currentResponse'], config['textTemplate'])

    if config['gab'] :
        say(config)
