
# Bodged English AI Coach

Bodged English AI Coach is an unique CLI based tool, going to study foreign languages.

"No shiny UI, no fluff: just raw AI conversations, instant grammar corrections, and vocabulary drills, all wrapped in a gloriously “bodged” but surprisingly effective package. Perfect for hackers, minimalists, and anyone who learns better without the distraction of a GUI." (deepseek cuts)

## Requirements

* Linux (able to play mp3 files)
* Ollama (running to serve)
* a local LLM model (e.g. Gemma3:4b)
* good mood and tolerance of Google's Lady

## Installation

* Clone the repository
* Satisfy [linux dependencies](docs/ubuntu_required.txt)
* Install [python libs](docs/py_required.txt)

## Creating a lesson 

To create a lesson via LLM, find a English text and run:

```
./build.sh <english_text_file.txt> <lesson_name>
```

note: In advance put unknown words into square brackets. This will be used to form a word set to learn.


## Using

To run:

```
./coach.sh 
```

At the first stage choose a lesson (number), then navigate with keyword (press enter as needed).

Text menu:
* listen to the text (s)
* display it, if goes away (p)
* say a specific phrase (a)
* translate the text (T) or a given sentence (t)
* explain a given word (x)
* query the llm (l)
* exit (e)

Either Questions (q) or Words (w) menu:
* say question (sq) or answer (sa)
* display them (pq) (pa)
* move to the next item (n)
* constract a sentence and check via llm (c)
* translate (t), explain (x) a word/sentence
* go to main menu (m) or exit (e)


Enjoy.



