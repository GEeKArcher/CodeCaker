import os

def run(solution, brute, generator):
    for _ in range(10000):
        s="g++ "+str(generator)
        os.system(s)
        os.system("./a.out >ip1.txt")
        t="g++ "+str(solution)
        os.system(t)
        os.system("./a.out <ip1.txt >ot1.txt")
        u = "g++ " + str(brute)
        os.system(u)
        os.system("./a.out <ip1.txt >ot2.txt")