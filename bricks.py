import db_con
from psycopg2.extras import RealDictCursor

def allBricks():
    sql = "select * from brick_types"
    list = []
    cnx = db_con.create_connection("warsztat1")
    crs = cnx.cursor(cursor_factory=RealDictCursor)
    crs.execute(sql)
    for row in crs:
        list.append({"brick_type_id": row["brick_type_id"],
                     "brick_type": row["brick_type"]})
    crs.close()
    cnx.close()
    return list

def addBrick(number_of_throws, brick_type, number_to_add):
    brick = nameBrick(number_of_throws, brick_type, number_to_add)
    sql = f"insert into bricks(brick_type_id, number_of_throws, number_to_include, brick_name) values ({brick_type}, {number_of_throws}, {number_to_add}, '{brick}') returning brick_id"

    cnx = db_con.create_connection("warsztat1")
    cursor = cnx.cursor()

    cursor.execute(sql)

    cursor.close()
    cnx.close()



def nameBrick(number_of_throws, b_type, number_to_add):
    brick = ""
    sql = f"select brick_type from brick_types where brick_type_id = {b_type}"
    cnx = db_con.create_connection("warsztat1")
    crs = cnx.cursor(cursor_factory=RealDictCursor)

    crs.execute(sql)
    for row in crs:
        b_type = row['brick_type']
    crs.close()
    cnx.close()

    if number_of_throws == "1" and number_to_add == "0":
        brick = f"D{b_type}"
    elif number_of_throws == "1" and int(number_to_add)>0:
        brick = f"D{b_type}+{number_of_throws}"
    elif number_of_throws == "1" and int(number_to_add)<0:
        brick = f"D{b_type}{number_to_add}"
    elif number_to_add == "0":
        brick = f"{number_of_throws}D{b_type}"
    elif int(number_to_add) > 0:
        brick = f"{number_of_throws}D{b_type}+{number_to_add}"
    else:
        brick = f"{number_of_throws}D{b_type}{number_to_add}"

    return brick

print(nameBrick('1',2,'-1'))

addBrick("1",1,"0")
