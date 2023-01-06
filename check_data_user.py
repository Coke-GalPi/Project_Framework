from connection import DAO
from werkzeug.security import check_password_hash
dao = DAO()

def check_data_user(username, password_user):
    filter_user = dao.authentication(username)
    if filter_user:
        same_passw = check_password_hash(filter_user[6], password_user)
        if same_passw == True:
            return filter_user
    return None