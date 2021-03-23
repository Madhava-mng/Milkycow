from hashlib import sha1
from random import randint, choice

def enc(string, passwd="pass ", rotate=500):
    passwd = sha1((str(passwd)+"#@").encode()).hexdigest()
    mkrnd = lambda:chr(choice([
        randint(2, 39),
        randint(2, 255),
        randint(200000, 205000)
        ]))
    mkstr = ""
    mkslt = ""
    inject = ""
    mkvsp = 1

    for i in range(1, 11):
        if(rotate%i == 0):
            mkvsp = i

    def mkslt(val, t="", T=""):
        for i in range(6):
            t += mkrnd()
            T += mkrnd()
        return "Salted__"+t+val+T
    tmp = ''
    pas = 0

    for i in passwd:
        if(i.isdigit()):
            if(i == mkvsp):
                continue
            pas += ord(i)
        else:
            pas -= ord(i)
        while(pas <= 0):
            pas += len(passwd)+ord(i)

    for s in string:
        for i in range(mkvsp):
            inject += mkrnd()
        mkstr += (s+inject)
        inject = ""

    for i in str(mkstr):
        tmp += chr(ord(i)+rotate+pas)

    return mkslt(tmp)


