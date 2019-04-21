import math

from Crypto.Cipher import AES

KEY = 'DEB536FA9890D43B'
INITIAL_VALUE = '6C0AF5F86C504961'


def encrypt(text):
    aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)
    padding_threshold = int(math.ceil(len(text) / 16.0) * 16)
    return aes.encrypt(text.ljust(padding_threshold))


def decrypt(cipher_text):
    aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)
    return aes.decrypt(cipher_text).rstrip()
