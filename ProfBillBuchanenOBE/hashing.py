import sys
import bcrypt
import binascii

from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2, scrypt, HKDF

#make a filler password
password = 'qwerty'

#then they are going to make a salt through the random function
salt = get_random_bytes(16)

#not sure what this is
s = ""

#not sure what this is
type = 1

#not sure what this is
bytes = 16

#not sure what any of this is
if (len(sys.argv) > 1):
    password = str(sys.argv[1])
    
if (len(sys.argv) > 2):
    s = str(sys.argv[2])
    
if (len(sys.argv) > 3):
    type = int(sys.argv[3])
    
if (len(sys.argv) > 4):
    bytes = int(sys.argv[4])
    
#not sure 
salt = binascii.unhexlify(s)

if (type == 1):
    
    KEK = PBKDF2(password, salt, bytes, count = 1000, hmac_hash_module=SHA256)
    print("Using PKDF2")
    
elif (type == 2):
    
    KEK = scrypt(password, salt, bytes, N = 2**14, r = 8, p = 1)
    print("Using Scrypt")
    
elif (type == 3):
    
    KEK = bcrypt.kdf(password = password.encode(), salt = b'salt', desired_key_bytes = bytes, rounds = 100)
    print("Using bcrypt")
    
else:
    
    KEK = HKDF(password.encode(), bytes, salt, SHA256, 1)
    print("Using HKDF")
    
print(f"Password: {password}, Salt: {s}")
print("Hash:", binascii.hexlify(KEK))