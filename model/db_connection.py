import psycopg

class Connection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=bbdd_fastAPI user=postgres password=123456 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
    
    def __def__(self):
        self.conn.close()