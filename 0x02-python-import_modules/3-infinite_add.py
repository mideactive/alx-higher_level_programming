#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    add = 1
    for i in range(len(sys.argv) - 1):
        add += int(sys.argv[i + 1])
    print("{}".format(int(add)))
