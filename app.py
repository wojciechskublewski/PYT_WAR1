from flask import Flask
from flask import render_template
from flask import request
import random
import bricks
import result
from results import dbAdd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('start.html')

@app.route('/brick', methods=["GET"])
def doLosowania():
    brick_list = bricks.allBricksNames()
    return render_template('brick.html',brick_list= brick_list)

@app.route('/brick',methods=["POST"])
def losowanie():
    brick_id = request.form["brick_id"]
    list = bricks.queryBrick(brick_id)
    nbr_dice = random.randint(1, int(list[1].get("brick_type")))
    wynik = int(list[0].get("number_of_throws"))*nbr_dice + int(list[0].get('number_to_include'))
    final_result = {"brick": list[0].get("brick_name"),
                    "wynik": wynik,
                    "brick_id": brick_id}
    result.addResult(brick_id,wynik)
    return render_template("wynik.html", result = final_result)

@app.route("/addBrickType", methods=["GET"])
def addBrickTypeDet():
    brick_type_list = bricks.allBricks()
    return render_template("addBrickType.html", list = brick_type_list)

@app.route("/addBrickType", methods=["POST"])
def addBrickTypePost():
    brick_type = request.form["brick_type"]
    bricks.addBrickTypes(brick_type)
    return render_template("ok.html")

@app.route("/wynik", methods=["GET"])
def wynikD():
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
