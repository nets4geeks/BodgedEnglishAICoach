
import logging
import sys

import utl
import llm
import c
import d
import q
import t
import w
import conf
import ver


def main():

    print("\n::: build v"+ver.get()+" :::\n")

    config = conf.get(sys.argv[1],True)
    conf.init(sys.argv[2],sys.argv[3],config)


    words = w.getInitWords(config)
    w.save(words,config)

    t.save(config)

    crams = c.getCrams(config)
    c.save(crams, config)


    questions = llm.ask(config['questionsTemplate'], config)
    q.save(questions,config)

#    dialogs = llm.ask(config['dialogsTemplate'], config)
#    d.save(dialogs,config)

    conf.log("| build | "+config['name'], config)

main()