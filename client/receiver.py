import binascii
import os
import struct

from scapy.all import ShortField, IntField, FieldListField, FieldLenField
from scapy.all import sniff, get_if_list
from scapy.layers.inet import IPOption, TCP, _IPOption_HDR

from client.blindbox import TYPE_BLINDBOX
from .aes import encrypt, decrypt


def get_if():
    ifs = get_if_list()
    iface = None
    for i in ifs:
        if "eth0" in i:
            iface = i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface


class IPOption_MRI(IPOption):
    name = "MRI"
    option = 31
    fields_desc = [_IPOption_HDR,
                   FieldLenField("length", None, fmt="B",
                                 length_of="swids",
                                 adjust=lambda pkt, l: l + 4),
                   ShortField("count", 0),
                   FieldListField("swids",
                                  [],
                                  IntField("", 0),
                                  length_from=lambda pkt: pkt.count * 4)]


class BlindBoxSession:
    def __init__(self):
        self.received_tokens = []
        self.generated_tokens = []
        self.is_valid = True

    def add_token(self, token):
        self.received_tokens.append(token)

    def validate(self, payload):
        print "Validating session"
        for i in range(len(payload)):
            self.generated_tokens.append(encrypt(payload[i:i + 8]))

        self.is_valid = self.received_tokens == self.generated_tokens


session = BlindBoxSession()


def handle_pkt(pkt):
    global session
    if TCP in pkt:
        if ('\x00' + bytes(pkt[TCP].payload)[:3]) == struct.pack(">L", TYPE_BLINDBOX):
            token = str(pkt[TCP].payload)[3:]
            session.add_token(token)
            print "Got a BlindBox packet with token %s" % ("128w0x" + binascii.hexlify(token))
        else:
            payload = decrypt(str(pkt[TCP].payload))
            session.validate(payload)
            print "Got a %s TCP packet with payload \"%s\"" % ("VALID" if session.is_valid else "MALICIOUS", payload)
            session = BlindBoxSession()


def main():
    ifaces = filter(lambda i: 'eth' in i, os.listdir('/sys/class/net/'))
    iface = ifaces[0]
    print "Sniffing on %s" % iface
    sniff(iface=iface,
          prn=lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()
