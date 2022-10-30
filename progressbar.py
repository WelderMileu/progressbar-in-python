#!/usr/bin/python3
import numpy as np
from time import sleep

def main():
    try:
        range_n = np.arange(80)
        bar = []

        for x in range(80):
            bar.append('▒')

        print()
        for x in range_n:
            print("|{} \r".format("".join(bar)), end='')
            bar[x]  = "█"
            bar[-1] = " [{}%/{}%]".format(str(x), 78)
            sleep(.1)

        print()

    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
