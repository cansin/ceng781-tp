import math

from Crypto.Cipher import AES

KEY = 'This is a key123'
INITIAL_VALUE = 'This is an IV456'

aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)

def encrypt(text):
    padding_threshold = int(math.ceil(len(text) / 16.0) * 16)
    return aes.encrypt(text.ljust(padding_threshold))

def decrypt(cipher_text):
    return aes.decrypt(cipher_text).rstrip()