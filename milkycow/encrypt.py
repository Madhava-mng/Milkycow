from hashlib import sha1
from random import randint, choice

def enc(string, passwd="pass ", rotate=500):
    passwd = sha1((str(passwd)+"#@").encode()).hexdigest()
    mkrnd = lambda:chr(choice([
        randint(2, 39),
        randint(200000, 205000)
        ]))
    mkstr = ""
    mkslt = ""
    for s in string:
        mkstr += (s+mkrnd())

    def mkslt(val, t="", T=""):
        for i in range(6):
            t += mkrnd()
            T += mkrnd()
        return "Salted__"+t+val+T
    tmp = ''
    pas = 0

    for i in passwd:
        if(i.isdigit()):
            if(i == '7'):
                continue
            pas += ord(i)
        else:
            pas -= ord(i)
        while(pas <= 0):
            pas += len(passwd)+ord(i)

    for i in str(mkstr):
        tmp += chr(ord(i)+rotate+pas)

    return mkslt(tmp)

