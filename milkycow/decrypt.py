from hashlib import sha1
from random import randint, choice

def dec(string, passwd='pass ', rotate=500):
    try:
        passwd = sha1((str(passwd)+"#@").encode()).hexdigest()
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
        tmp = ""
        mkstr = string[14:-6]
        for i in range(len(mkstr)):
            if(i%2 == 0):
                tmp += chr(ord(mkstr[i])-rotate-pas)
    except:
        tmp = enc("".join([chr(randint(40, 255)) for x in range(len(str(string))-20)]), "", rotate)
    return tmp

