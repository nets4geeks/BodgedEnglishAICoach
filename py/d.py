
import uuid
import json
import logging

import utl

def add (dialogs):
    dialogsList = []
    for qa in dialogs['dialogs']:
        qa['utterance1ID'] = uuid.uuid4().hex[:16]
        qa['utterance2ID'] = uuid.uuid4().hex[:16]
        qa['utterance3ID'] = uuid.uuid4().hex[:16]
        qa['utterance4ID'] = uuid.uuid4().hex[:16]
        dialogsList.append(qa)
    return {'dialogs': dialogsList }


def save(dialogs, config):
    logging.info("saving dialogs" )
    new = add(dialogs)
    utl.saveFile(config['dialogsFile'],  json.dumps(new, indent=4))

