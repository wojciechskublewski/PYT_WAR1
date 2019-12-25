import db_con
import datetime

from psycopg2.extras import RealDictCursor

def addResult(brick_id, result, user_id=1):
    sql = f"insert into brick_results(brick_id, user_id, result_date, result_time, result) values ('{brick_id}', '{user_id}', '{datetime.datetime.now().date()}', '{datetime.datetime.now().time().strftime('%H:%M:%S')}','{result}') returning result_id"
    cnx = db_con.create_connection("warsztat1")
    cursor = cnx.cursor()

    cursor.execute(sql)

    cursor.close()
    cnx.close()




addResult(1,5,1)

print(datetime.datetime.now().date())