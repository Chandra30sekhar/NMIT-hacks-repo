import hashlib

def ret_sha1(passwrd):
    return hashlib.sha1(passwrd.encode()).hexdigest()