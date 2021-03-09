from random import randint as rint
from random import choice
from codelib.base import base64decode as b_dec
from codelib.base import base64encode as b_enc
from codelib.rot import *
def salt(string, rot):
    v = choice(("Salted__",
         "".join([chr(rint(3, 30)) for x in range(8)]),
         "".join([chr(rint(30, 80)) for x in range(8)]),
         "".join([chr(rint(80, 100)) for x in range(8)]),
         "".join([chr(rint(100, 200000)) for x in range(8)])
        ))
    v += "".join([chr((
        choice((rint(3, 255), 200000, rint(2, 35), rint(2, 255) )))) for x in range(10)])
    v += string
    v += "".join([chr(rint(3, 30)) for x in range(5)])
    v += "".join([chr(
        choice((rint(3, 60),200000,))) for x in range(5)])
    v += "".join([chr(rint(2, 60)) for x in range(13)])
    v += "".join([chr(
        choice((200000,200001,rint(2, 30)))) for x in range(2)])

    return rot47IterForword(b_enc(v), rot)
def enc(string, password = 'foo bar moooo', rotate = 50, layer = 0, rfs=6):
    tmp = ""
    tmp_key = 0
    try:
        if(layer >= 0):
            for x in bytearray(password.encode()):
                tmp_key += x
            for i in string:
                tmp += chr(ord(i) + tmp_key + rotate)
            return enc(salt(tmp, rfs), password, rotate, layer - 1, rfs)
        return string
    except KeyboardInterrupt:
        return "interrupt :: form keyboard"
    except:
        return enc(string, password, rotate, layer, rfs)


