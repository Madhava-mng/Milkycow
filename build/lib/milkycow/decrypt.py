from hashlib import sha1
from random import randint, choice

def dec(string, passwd='pass ', rotate=500):
    try:
        passwd = sha1((str(passwd)+"#@").encode()).hexdigest()
        pas = 0
        mkvsp = 1
        tmp = ""
        mkstr = string[14:-6]

        for i in range(1, 11):
            if(rotate%i == 0):
                mkvsp = i

        for i in passwd:
            if(i.isdigit()):
                if(i == mkvsp):
                    continue
                pas += ord(i)
            else:
                pas -= ord(i)
            while(pas <= 0):
                pas += len(passwd)+ord(i)

        for i in range(len(mkstr)):
            if(i%(mkvsp+1) == 0):
                tmp += chr(ord(mkstr[i])-rotate-pas)

    except:
        tmp = "".join([chr(randint(95, 123)) for x in range(len(str(string))+randint(1,20))])
    return tmp


