import db_con
from psycopg2.extras import RealDictCursor

def allBricks():
    sql = "select * from brick_types"
    list  = []
    cnx = db_con.create_connection("warsztat1")
    crs = cnx.cursor(cursor_factory=RealDictCursor)
    crs.execute(sql)
    for row in crs:
        list.append({"brick_type_id": row["brick_type_id"],
                     "brick_type": row["brick_type"]})
    crs.close()
    cnx.close()
    return list


for i in allBricks():
    print(i["brick_type"])
