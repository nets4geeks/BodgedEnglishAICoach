

from jinja2 import Template
import requests

import yaml
import logging
import sys
import re


def ask(templateName, config):
    path = "./templates/"+templateName

    logging.info("creating prompt from "+path)
    with open(path, 'r') as f:
        prompt = Template(f.read()).render(config)


    payload = {
       "model":  config['model'],
       "prompt": prompt,
       "stream": False
    }

    if config['temperature'] != None:
        payload["temperature"]=config['temperature']


    logging.info("asking "+config['model']+" via "+config['url'])
    print("asking llm, please wait...")
    response = requests.post(config['url'], json=payload)

#    print (response.json()['response'])

    pattern = r"```yaml\n(.*?)```"
    match = re.search(pattern, response.json()['response'], re.DOTALL)

    if not (match):
        logging.error('no yaml block found: \n'+response.json()['response'])
        exit(1)

    return yaml.safe_load(match.group(1).strip())



def ask2(templateName, config):
    path = "./templates/"+templateName

    logging.info("creating prompt from "+path)
    with open(path, 'r') as f:
        prompt = Template(f.read()).render(config)


    payload = {
       "model":  config['model'],
       "prompt": prompt,
       "stream": False
    }

    if config['temperature'] != None:
        payload["temperature"]=config['temperature']


    logging.info("asking "+config['model']+" via "+config['url'])
    print("asking llm, please wait...")
    response = requests.post(config['url'], json=payload)

    return response.json()['response']
