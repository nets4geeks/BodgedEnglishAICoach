
import uuid
import json
import logging
import utl

import inf
import tts
import llm

def add (questions):
    questionsList = []
    for qa in questions['questions']:
        qa['questionID'] = uuid.uuid4().hex[:16]
        qa['answerID'] = uuid.uuid4().hex[:16]
        questionsList.append(qa)

    return {'questions': questionsList }

def save(questions, config):
    logging.info("saving questions" )
    new = add(questions)
    utl.saveFile(config['questionsFile'],  json.dumps(new, indent=4))

def load(config):
    logging.info("reading questions file" )
    config['questions'] = json.loads(utl.readFile(config['questionsFile']))['questions']


def show(n, typ, config):
    if typ == 'q':
        inf.show("Question", n, config['questions'][n]['questionID'], config['questions'][n]['question'], config['textTemplate'])
    if typ == 'a':
        inf.show("Answer", n, config['questions'][n]['answerID'], config['questions'][n]['answer'], config['textTemplate'])
    if config['gab'] :
        say(n, typ, config)


def say(n, typ, config):
    if typ == 'q':
        tts.say(config['questions'][n]['questionID'], config['questions'][n]['question'], config)
    if typ == 'a':
        tts.say(config['questions'][n]['answerID'], config['questions'][n]['answer'], config)

def findex(config):
    return len(config['questions'])-1


