from flask import Flask, render_template
from utils import occupations
app = Flask(__name__)
@app.route("/occupations")
def main():
    return render_template("occupations.html", title = "Occupations", L = occupations.updateList(), randjob = occupations.randchooser())

if __name__ == '__main__':
    app.run(debug = True)

