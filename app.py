from flask import Flask
from flask import render_template
import random
from results import dbAdd
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('start.html')

@app.route("/wynik")
def wynik6D():
    result = random.randint(1, 6)
    dbAdd("warsztat1",result)
    return render_template("wynik.html", result =result)

if __name__ == '__main__':
    app.run()
