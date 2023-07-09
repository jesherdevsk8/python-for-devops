#!/usr/bin/env python3

import psutil
from prettytable import PrettyTable

# Get disk usage information
disk_usage = psutil.disk_partitions(all=True)
# disk_usage = psutil.disk_partitions()


def _convert_bytes(num):
    """
    Helper function to convert bytes to a human-readable format.
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}B"
        num /= 1024.0
    return f"{num:.1f} YB"

# Create table
table = PrettyTable()
table.field_names = ['Mounted on', 'Filesystem', 'Type', 'Size', 'Used', 'Free', 'Percent']
for partition in disk_usage:
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        table.add_row([partition.device, partition.fstype, _convert_bytes(usage.total),
                       _convert_bytes(usage.used), _convert_bytes(usage.free),
                       f"{usage.percent}%", partition.mountpoint])
                      #  f"{usage.percent}% {'█'*round(usage.percent)}", partition.mountpoint])
    except PermissionError:
        pass


# Print table
print(table)
