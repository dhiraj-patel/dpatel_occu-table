import random

qwer = open("data/occupations.csv",'r')
file = qwer.readlines()
qwer.close()
def updateList():
    t = 0
    L=[]
    for row in file[1:-1]:
        num = int(10 * float(row[row.rfind(',')+1:]))
        start = t
        t = num + start
        L.append([start, t, row[:row.rfind(',')]])
    return L

def randchooser():
    rand = random.random() * 1000
    L = updateList()
    for row in L:
        if rand > row[0] and rand < row[1]:
            return row[2]

