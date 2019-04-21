import math

from Crypto.Cipher import AES
from Crypto.Hash import MD5

KEY = 'DEB536FA9890D43B'
INITIAL_VALUE = '6C0AF5F86C504961'


def token(text):
    h = MD5.new()
    h.update(encrypt(text))
    return h.digest()


def encrypt(text):
    aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)
    padding_threshold = int(math.ceil(len(text) / 16.0) * 16)
    return aes.encrypt(text.ljust(padding_threshold))


def decrypt(cipher_text):
    aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)
    return aes.decrypt(cipher_text).rstrip()
