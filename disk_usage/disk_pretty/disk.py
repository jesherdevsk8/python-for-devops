#!/usr/bin/env python3

import os
import psutil
from prettytable import PrettyTable

yellow = '\033[1;33m'
green = '\033[0;32m'
reset = '\033[0;0m'

print(yellow + 'Hello, ' + os.getlogin() + '!\nThis is your custom disk space information' + reset, '\n')

def _convert_bytes(num):
    # Helper function to convert bytes to a human-readable format.
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}B"
        num /= 1024.0
    return f"{num:.1f} YB"

base_partitions = ['/', os.environ['HOME']]
# Create table
table = PrettyTable()
table.field_names = ['Mounted on',  'Total', 'Used', 'Free', 'Percent']

for partition in base_partitions:
    try:
      usage = psutil.disk_usage(partition)
      table.add_row([partition, _convert_bytes(usage.total),
          _convert_bytes(usage.used),
          _convert_bytes(usage.free),
          f"{usage.percent}%"
      ])
    except PermissionError:
        print(f"Permission denied for partition: {partition}")

print(f"{green}{table}{reset}")