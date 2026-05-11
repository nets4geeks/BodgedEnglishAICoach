
# coacher

import logging
import sys

import utl
import llm
import d
import q
import t
import w
import conf
import tts

def M(config):
    t.show(config)
    while True:
        i = input("[s]ay/[p]rint [a]udio/e[x]plain/[T|t]ranslate/[l]lm [q]uestions/[w]ords [e]xit\n$ ")

        if (i == 'say') or (i == 's'):
            t.say(config)

        if (i == 'print') or (i == 'p'):
            t.show(config)

        if (i == 'questions') or (i == 'q'):
            Q(config)

        if (i == 'words') or (i == 'w'):
           if w.notEmpty(config):
                W(config)
           else:
                print("no words to learn :((")


        if (i == 'audio') or (i == 'a'):
            k = input("type a phrase to say: ")
            tts.tmp(k,config)

        if (i == 'translate') or (i == 't'):
            k = input("type a phrase to translate: ")
            t.translate(k, config)

        if (i == 'T') or (i=="Translate"):
            t.translateText(config)


        if (i == 'explain') or (i == 'x'):
            k = input("type a word to explain: ")
            t.clarify(k, config)


        if (i == 'llm') or (i == 'l'):
            k = input("type a prompt to llm: ")
            t.query(k, config)

        if (i == 'exit') or (i == 'e'):
           exit(0)


def W(config):
    current = 0
    final = w.findex(config)
    w.show(current,'q',config)
    while True:
        i = input("[sq]uestion/[sa]nswer/[pq]estion/[pa]nswer/[n]ext [a]udio/[c]heck/e[x]plain/[t]ranslate/[l]lm [m]enu/[e]xit\n$ ")


        if (i == 'menu') or (i == 'm'):
            M(config)

        if (i == 'exit') or (i == 'e'):
            exit(0)

        if (i == 'pquestion') or (i == 'pq'):
            w.show(current,'q',config)
        if (i == 'panswer') or (i == 'pa'):
            w.show(current,'a',config)


        if (i == 'squestion') or (i == 'sq'):
            w.say(current,'q',config)
        if (i == 'sanswer') or (i == 'sa'):
            w.say(current,'a',config)

        if (i == 'next') or (i == 'n'):
           if current < final:
                current = current+1
                w.show(current,'q',config)
           else:
                print("\nurra! there's no word. type [m]enu to return or [e]xit to leave\n")
                if config['gab'] :
                    tts.say("complited","Task completed! Type 'm' for menu or 'e' to exit", config)

        if (i == 'audio') or (i == 'a'):
            k = input("type a phrase to say: ")
            tts.tmp(k,config)

        if (i == 'translate') or (i == 't'):
            k = input("type a phrase to translate: ")
            t.translate(k, config)

        if (i == 'explain') or (i == 'x'):
            k = input("type a word to explain: ")
            t.clarify(k, config)


        if (i == 'check') or (i == 'c'):
            k = input("type a sentence for checking: ")
            t.check(k,config)


def Q(config):
    current = 0
    final = q.findex(config)
    q.show(current,'q',config)
    while True:
        i = input("[sq]uestion/[sa]nswer/[pq]estion/[pa]nswer/[c]heck/[n]ext [a]udio/e[x]plain/[t]ranslate/[l]lm [m]enu/[e]xit\n$ ")

        if (i == 'pquestion') or (i == 'pq'):
            q.show(current,'q',config)
        if (i == 'panswer') or (i == 'pa'):
            q.show(current,'a',config)

        if (i == 'squestion') or (i == 'sq'):
            q.say(current,'q',config)
        if (i == 'sanswer') or (i == 'sa'):
            q.say(current,'a',config)


        if (i == 'next') or (i == 'n'):
           if current < final:
                current = current+1
                q.show(current,'q',config)
           else:
                print("\nurra! there's no questions. type [m]enu to return or [e]xit to leave\n")
                if config['gab'] :
                    tts.say("complited","Task completed! Type 'm' for menu or 'e' to exit", config)

        if (i == 'check') or (i == 'c'):
            k = input("type a sentence for checking: ")
            t.check(k,config)

        if (i == 'menu') or (i == 'm'):
            M(config)

        if (i == 'audio') or (i == 'a'):
            k = input("type a phrase to say: ")
            tts.tmp(k,config)

        if (i == 'translate') or (i == 't'):
            k = input("type a phrase to translate: ")
            t.translate(k, config)

        if (i == 'explain') or (i == 'x'):
            k = input("type a word to explain: ")
            t.clarify(k, config)

        if (i == 'llm') or (i == 'l'):
            k = input("type a prompt to llm: ")
            t.query(k, config)


        if (i == 'exit') or (i == 'e'):
            exit(0)


def main():

    config = conf.get(sys.argv[1])

    lessons = t.printLessons(config)

    i = int(input("enter lesson's number: "))

    conf.load(lessons[i],config)

    M(config)

main()