
# cli interface

import logging
from jinja2 import Template

def show(title, name, id, text, templateName):
    path = "./templates/"+templateName

    logging.info("render screen from "+path)
    with open(path, 'r') as f:
        output = Template(f.read()).render({ 'title': title, 'name': name, 'id': id, 'text': text})

    print(output)

