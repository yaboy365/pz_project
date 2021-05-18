import sqlite3

import pytest


def check_credentials(login, password):
    conn = sqlite3.connect('credentials.db')
    c = conn.cursor()
    r = c.execute("SELECT password FROM Credentials WHERE login=(?)", (login,))
    password_from_db = ''
    for row in r:
        password_from_db = row[0]

    if password == password_from_db:
        return True
    else:
        return False

@pytest.mark.login
def test_admin():
    login='admin'
    password='admin'
    assert check_credentials(login,password)==True

def test_pielegniarka():
    login='pielegniarka'
    password='pielegniarka'
    assert check_credentials(login,password)==True

def test_fail():
    login='falszywy'
    password='oszust'
    assert check_credentials(login, password) == False