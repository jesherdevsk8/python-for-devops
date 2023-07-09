#!/usr/bin/env python3

## create files with bash
## touch ./manage_files/caralho{0..10}.py

for i in range(1, 6):
    filename = f"file{i}.rb"
    with open(filename, "w") as file:
        file.write(f"This is file {i}\n")
