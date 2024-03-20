import os

import random

for n in range(2, 3000):
    for test in range(10):
        args = list(range(n))
        if (test == 0):
            args = args[::-1]
        else:
            random.shuffle(args)
        oargs = args
        args = [str(x) for x in args]
        args = " ".join(args)
        cmd = "../PmergeMe " + args + " > out.txt"
        os.system(cmd)
        after = open("out.txt").read().split("After   :")[1].split("\n")[0]
        after = after.split(" ")
        after = [int(x) for x in after if x.strip()]
        if (after != sorted(oargs)):
            print (cmd)
            exit()
        print ("OK", "n: ", n, "test: ", test)