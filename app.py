from flask import Flask
from flask import render_template
from flask import request
import random
import bricks
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

@app.route("/addBrick",methods=["GET"])
def addBrickGet():
    list = bricks.allBricks()
    return render_template("addBrick.html",list=list)

@app.route("/addBrick",methods=["POST"])
def addBrickPost():
    brick_type_id = request.form["brick_type"]
    number_of_throws = request.form['nbr_throws']
    number_to_add = request.form['nbr_help']

    bricks.addBrick(number_of_throws,brick_type_id,number_to_add)

    return render_template("ok.html")


if __name__ == '__main__':
    app.run()
