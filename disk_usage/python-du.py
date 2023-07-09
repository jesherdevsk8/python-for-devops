#!/usr/bin/env python3

import os

#command="du -sh"

#while True:
#  if os.system(command) != 0:
#    print("Failed execute command: " + command)
#    exit(-1)

commands = ["ls -l", "uname", "ps"]

for arg in commands:
  if os.system(arg) != 0:
    print("Failed to execute command : " + arg)
    exit(-1)

path="/tmp"
os.statvfs(path)
