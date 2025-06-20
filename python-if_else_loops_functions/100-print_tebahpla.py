#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 0:
        # Even index -> lowercase
        print("{}".format(chr(i + 97)), end="")
    else:
        # Odd index -> uppercase
        print("{}".format(chr(i + 65)), end="")
