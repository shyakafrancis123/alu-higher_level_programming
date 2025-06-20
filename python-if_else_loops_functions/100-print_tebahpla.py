#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 0:
        # even index: lowercase
        print("{}".format(chr(i + 97)), end="")
    else:
        # odd index: uppercase
        print("{}".format(chr(i + 65)), end="")
