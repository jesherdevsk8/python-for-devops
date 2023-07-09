#!/usr/bin/env python3

import os

yellow = '\033[1;33m'
green = '\033[0;32m'
reset = '\033[0;0m'

print(yellow + 'Hello, ' + os.getlogin() + '! How are you?' + reset, '\n')

base_partitions = ['/', os.environ['HOME']]

for partition in base_partitions:
  # Get disk usage information from
  disk_usage = os.statvfs(partition)
  total_size = disk_usage.f_frsize * disk_usage.f_blocks
  free_size  = disk_usage.f_frsize * disk_usage.f_bfree
  used_size  = total_size - free_size

  # Print disk usage information from /
  print(green + f"Total disk space in {partition}: {total_size / (1024 ** 3):.2f} GB" + reset)
  print(green + f"Used disk space in {partition}: {used_size / (1024 ** 3):.2f} GB" + reset)
  print(green + f"Free disk space in {partition}: {free_size / (1024 ** 3):.2f} GB", '\n' + reset)
