#!/usr/bin/env python3

import shutil

root_total, root_used, root_free = shutil.disk_usage('/')
home_total, home_used, home_free = shutil.disk_usage('/home')

print("/")
print("Total: %d GiB" % (root_total // (2**30)))
print("Used: %d GiB" % (root_used // (2**30)))
print("Free: %d GiB" % (root_free // (2**30)), "\n")

print("/Home")
print("Total: %d GiB" % (home_total // (2**30)))
print("Used: %d GiB" % (home_used // (2**30)))
print("Free: %d GiB" % (home_free // (2**30)))
