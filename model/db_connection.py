import psycopg

class Connection():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=bbdd_fastAPI user=postgres password=123456 host=localhost port=5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    def insert_user(self, data_user):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "users" (rut_user, name_user, surname_user, telephone_user, 
                username_user, pass_user, status_user) VALUES (%(rut_user)s,%(name_user)s,
                %(surname_user)s,%(telephone_user)s,%(username_user)s,%(pass_user)s,
                %(status_user)s)
                """, data_user)
        self.conn.commit()
    
    def insert_document(self, data_document):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "documents" (type_document, teacher_document, name_document, theme_document,
                directory_document) VALUES (%(type_document)s,%(teacher_document)s,%(name_document)s,
                %(theme_document)s,%(directory_document)s""", data_document)
        self.conn.commit()

    def __def__(self):
        self.conn.close()