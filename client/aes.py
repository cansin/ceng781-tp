from Crypto.Cipher import AES

KEY = 'This is a key123'
INITIAL_VALUE = 'This is an IV456'

aes = AES.new(KEY, AES.MODE_CBC, INITIAL_VALUE)

def encrypt(text):
    return aes.encrypt(text)

def decrypt(cipher_text):
	return aes.decrypt(cipher_text)