#!/usr/bin/bash

if [ $# -ne 2 ]
  then
    echo "Usage: `basename $0` english_text_filename.txt lesson_name"
    exit $E_WRONG_ARGS
fi

python py/build.py config.yml ${1} ${2}
