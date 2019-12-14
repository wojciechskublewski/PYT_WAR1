from psycopg2 import connect, OperationalError
def create_connection(db_name):
    username = "postgres"
    passwd = "coderslab"
    hostname = "127.0.0.1"
    try:
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cnx.autocommit = True
        return cnx
    except OperationalError as error:
        print(error)