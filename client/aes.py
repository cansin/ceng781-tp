import math

from Crypto.Cipher import AES

KEY = 'DEB536FA9890D43BEED9654AF0DBFC6A'
INITIAL_VALUE = '6C0AF5F86C504961204B1A42D8B99530'

aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)

def encrypt(text):
    padding_threshold = int(math.ceil(len(text) / 16.0) * 16)
    return aes.encrypt(text.ljust(padding_threshold))

def decrypt(cipher_text):
    return aes.decrypt(cipher_text).rstrip()