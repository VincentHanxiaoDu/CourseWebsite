from config import db

def getInstructor(username, password):
    return getUser('instructor', username, password)


def getStudent(username, password):
    return getUser('students', username, password)


def getUser(table, username, password):
    users = db.engine.execute("SELECT * FROM {} WHERE username=? AND password=?".format(table), (username, password))
    user = users.first()
    info = None
    if user:
        attrs = users.keys()
        user = list(user)
        info = dict(zip(attrs, user))
    users.close()
    return info

def registerUser(table, username, password, firstname, lastname, **kwargs):
    return True