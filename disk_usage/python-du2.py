#!/usr/bin/env python3

from pprint import pprint
import subprocess
import os

def du(location: str):
    p = subprocess.Popen(["du", "-d", "1", location], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    return out.decode().splitlines()

def check_disk_usage(disk_usage: list):
    return {
        'Total': disk_usage.f_frsize * disk_usage.f_blocks,
        'Used': disk_usage.f_frsize * disk_usage.f_bfree,
        'Free': disk_usage.f_frsize * (disk_usage.f_blocks - disk_usage.f_bfree)
    }
        
def bar_graph(du_output: list, location: str):
    du_dict = { key: float(value)
                for value, key
                in map(lambda line: line.split("\t"), du_output) }

    total_value = sum(du_dict.values())
    name_width  = max(len(key) for key in du_dict.keys())
    percentages = { key: (value / total_value) * 100
                    for key, value in du_dict.items() }
    print("--------------------------")
    print("percentages:")
    pprint(percentages)
    print("--------------------------")
    print("bar graph:")
    for key in sorted(percentages.keys()):
        value       = round(percentages[key])
        disk_usage  = os.statvfs(key)
        hash_size = check_disk_usage(disk_usage)
        rounded_result = round(hash_size['Total'] / (1024 ** 3))

        print(f"{key:{name_width}}: {value:3d}% {'█'*round(value)}")
        
        ## hash_size = {'Total': 138074083328, 'Used': 65803325440, 'Free': 72270757888}
        ## list(hash_size) converts dictionary to a list
        # print(list(hash_size)[0], 'disk space', round(hash_size['Total'] / (1024 ** 3)))
        # print(list(hash_size)[1], 'disk space', round(hash_size['Used'] / (1024 ** 3)))
        # print(list(hash_size)[2], 'disk space', round(hash_size['Free'] / (1024 ** 3)))
        # print(hash_size)

if __name__ == "__main__":
    location = os.environ['HOME']
    du_output = du(os.path.join(location, 'Documentos'))
    print("--------------------------")
    print("du_output:")
    pprint(du_output)

    bar_graph(du_output, location)


# def disk():
#     for key in sorted(percentages.keys()):
#         disk_usage = os.statvfs(key)
#         total_size = disk_usage.f_frsize * disk_usage.f_blocks
#         free_size  = disk_usage.f_frsize * disk_usage.f_bfree
#         used_size  = total_size - free_size
#         print(total_size, '-', free_size, '-', used_size)

# def size():
#     for key in sorted(percentages.keys()):
#         disk_usage = os.statvfs(key)
#         print(check_disk_usage(disk_usage))
