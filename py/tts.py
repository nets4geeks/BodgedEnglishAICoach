
from gtts import gTTS
from pathlib import Path
import os
import logging

import utl


def say(id, text, config):

    fileName = config['ttsCache']+"/"+id+".mp3"

    if not (Path(fileName).is_file()):
       print ("rendering auido. please wait...")
       logging.info("rendering via "+config['ttsEngine']+" "+ fileName)
       if (config['ttsEngine'] == 'google'):
          tts = gTTS(text=text, lang='en', slow=False)
          tts.save(fileName)

    logging.info("saying item "+ fileName)
    print("saying (CTRL+C to interrupt)...")
    os.system("mpg123 -q "+fileName)


def tmp(text, config):

    fileName = config['ttsCache']+"/tmp.mp3"

    print ("rendering auido. please wait...")
    if (config['ttsEngine'] == 'google'):
        logging.info("rendering via google "+ fileName)
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(fileName)

    logging.info("saying "+ fileName)
    os.system("mpg123 -q "+fileName)

