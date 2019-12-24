import db_con
from psycopg2.extras import RealDictCursor

def addResult(brick_id, result):
    sql = f"insert into brick_results(brick_id, result) values ('{brick_id}', '{result}') returning result_id"
    cnx = db_con.create_connection("warsztat1")
    cursor = cnx.cursor()

    cursor.execute(sql)

    cursor.close()
    cnx.close()

