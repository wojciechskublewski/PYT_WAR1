
from db_con import create_connection


def dbAdd(db,result):
    cnx = create_connection(db)
    cursor = cnx.cursor()

    sql = f"insert into results(result) values ('{result}') returning results_id;"
    cursor.execute(sql)

    cursor.close()
    cnx.close()
