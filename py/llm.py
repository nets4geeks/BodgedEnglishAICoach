

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
       "think": config['think'],
       "stream": False
    }

    if config['temperature'] != None:
        payload["temperature"]=config['temperature']


    logging.info("asking "+config['model']+" via "+config['url'])
    print("asking llm, please wait...")

    headers = {}
    if config['key'] != None:
       headers['X-API-Key'] = config['key']
       
    response = requests.post(config['url'], headers=headers, json=payload)



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
       "stream": False,
       "think": config['think']
    }

    if config['temperature'] != None:
        payload["temperature"]=config['temperature']


    logging.info("asking "+config['model']+" via "+config['url'])
    print("asking llm, please wait...")


    headers = {}
    if config['key'] != None:
       headers['X-API-Key'] = config['key']

    response = requests.post(config['url'], headers=headers, json=payload)

    return response.json()['response']


def chat(config, msg):


    if len(config['context']) == 0:
        path = "./templates/"+config['chatInitTemplate']
        logging.info("creating chat from "+path)

        with open(path, 'r') as f:
           prompt = Template(f.read()).render(config)
    else:
        path = "./templates/"+config['chatTemplate']
        config['currentMessage'] = msg
        logging.info("creating chat from "+path)
        with open(path, 'r') as f:
           prompt = Template(f.read()).render(config)

    config['context'].append({"role": "user", "content": prompt})


    payload = {
       "model":  config['model'],
       "messages": config['context'],
       "think": config['think'],
       "stream": False
    }

    if config['temperature'] != None:
        payload["temperature"]=config['temperature']

    logging.info("asking "+config['model']+" via "+config['chat'])

    print("asking llm, please wait...")
#    print(payload)

    headers = {}
    if config['key'] != None:
       headers['X-API-Key'] = config['key']

    response = requests.post(config['chat'], headers=headers, json=payload)    
    print(response)
    assistant_message = response.json()['message']
    config['context'].append(assistant_message)

    return assistant_message['content']




