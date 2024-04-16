# crypto_password_compare.py
import sqlite3
import getpass
from passlib.hash import bcrypt

def read_passwords():
    """ Read passwords for all users from a password DB """
    # Using an sqlite db for demo purpose
    db = sqlite3.connect('passwd.db')
    cursor = db.cursor()
    hashes = {}
    for user, passwd in cursor.execute("SELECT user, password FROM passwds"):
        hashes[user] = bcrypt.hash(passwd, rounds=8)
    return hashes

def verify_password(user):
    """ Verify password for user """
    passwds = read_passwords()
    cipher = passwds.get(user)     # get the cipher
    if cipher and bcrypt.verify(getpass.getpass("Password: "), cipher):
        print('Password accepted')
    else:
        print('Wrong password, Try again')

if __name__ == "__main__":
    import sys
    verify_password(sys.argv[1])