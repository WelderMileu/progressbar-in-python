#!/usr/bin/python3
import numpy as np
from time import sleep
import requests
from sys import argv

def main(url, w):
    try:
        bar = []

        for x in range(100):
            bar.append('▒')
        
        f  = open(w, 'r')
        
        ls = []
        for x in f.readlines():
            ls.append(x.replace('\n', ''))
        print()

        c = []
        for count in range(100):
            value = (len(ls) * count) / 100
            c.append(int(value))

        r    = requests.get(url)
        code = r.status_code
        
        if code == 200:
            accept = []
            for x in ls:
                domain = "{}/{}".format(url, x)
                l      = requests.get(domain)
                code_l = l.status_code

                if code_l == 200:
                    accept.append(domain)

                for i in c:
                    if int(i) == ls.index(x):
                        print("|{} \r".format("".join(bar)), end='')
                        bar[c.index(i)]  = "█"
                        bar[-1] = " [{}/{}]".format(i, len(ls))
                        

            print()

        for x in accept:
            print(x)

    except Exception as err:
        print(err)

if __name__ == '__main__':
    url = argv[1]
    w   = argv[2]

    main(url, w)
