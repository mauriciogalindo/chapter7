import os

def run(**args):
    print "[*] In envinronment module."
    return str(os.environ)