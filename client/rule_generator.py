import binascii
import sys

from .aes import token


def main():
    print sys.argv

    if len(sys.argv) < 2:
        print 'pass 1 arguments: "<message>"'
        exit(1)

    cipher_text = token(sys.argv[1])
    print "128w0x" + binascii.hexlify(cipher_text)


if __name__ == '__main__':
    main()
