#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    with open(filename, encoding='utf-8') as f:
        l = len(f.read())
    return (l)
