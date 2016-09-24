from flask import Flask, render_template
app = Flask(__name__)

import random
qwer = open("occupations.csv",'r')
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
    rand = random.random() * 100
    L = updateList()
    for row in L:
        if rand < row[1] and rand > row[0] :
            return row[2]

@app.route("/occupations")
def main():
    return render_template("occupations.html", title="Occupations", L=updateList(), randjob = randchooser())



if __name__ == '__main__':
    app.run(debug=True)
