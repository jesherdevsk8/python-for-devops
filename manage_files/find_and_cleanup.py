#!/usr/bin/env python3

import os, subprocess, sys
from datetime import datetime, date

usage = '''\
	Usage: script.py --find or script.py --cleanup
	Options: --cleanup or --find '''

## change timestamps with touch
## touch -t 202301010000 ./manage_files/*.rb

## create files with bash first
## touch ./manage_files/file{0..10}.rb

currentpath = os.getcwd()
date_time   = datetime.now()
cleanup   	= f"find {currentpath} -mtime +10 -exec rm -rf {{}} \;"
just_find   = f"find {currentpath} -mtime +10"

# Check if command-line arguments were provided
if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg == "--cleanup":
      subprocess.run(cleanup, shell=True)
    elif arg == "--find":
      subprocess.run(just_find, shell=True)
    else:
      print("Invalid argument. Please provide --cleanup or --find.\n", usage)
else:
	print("No argument provided. Please provide --cleanup or --find.")
	print(usage)