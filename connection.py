import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'fastapi'
            )
        except Exception as exx:
            return ("ERROR al intentar la conexión: {0}".format(exx))

    def insert_new_User(self, data_user):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO USERS (RUT_USER,NAME_USER,SURNAME_USER,TELEPHONE_USER,USERNAME_USER,PASS_USER) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')"
                cursor.execute(sql.format(data_user[0],data_user[1],data_user[2],data_user[3],data_user[4],data_user[5]))
                self.connection.commit()
            except Error as ex:
                return ("ERROR: {0}".format(ex))

    def authentication(self, username):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM USERS WHERE USERNAME_USER = '{}'"
                cursor.execute(sql.format(username))
                return cursor.fetchone()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
        

    def insert_new_Document(self, data_document):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO DOCUMENTS (TYPE_DOCUMENT,TEACHER_DOCUMENT,NAME_DOCUMENT,THEME_DOCUMENT,FILE_DOCUMENT) VALUES ('{0}','{1}','{2}','{3}','{4}') "
                cursor.execute(sql.format(data_document[0],data_document[1],data_document[2],data_document[3],data_document[4]))
                self.connection.commit()
            except Error as ex:
                return ("ERROR: {0}".format(ex))
            
    def search_document(self, theme):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "SELECT * FROM DOCUMENTS WHERE THEME_DOCUMENT = '{}'"
                cursor.execute(sql.format(theme))
                return cursor.fetchall()
            except Error as ex:
                return ("ERROR: {0}".format(ex))