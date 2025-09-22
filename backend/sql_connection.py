 
import pymysql

__cnx = None
def get_sql_connection():
    print("----------Opening mysql connection")
    global __cnx
    if __cnx is None:
        __cnx = pymysql.connect(user='root', password='Rabaab@0505',
                              host='127.0.0.1',
                              database='gs')
    return __cnx
