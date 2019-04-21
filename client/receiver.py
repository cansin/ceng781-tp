import os
import struct
import sys

from scapy.all import ShortField, IntField, FieldListField, FieldLenField
from scapy.all import sniff, get_if_list
from scapy.layers.inet import IPOption, TCP, _IPOption_HDR

from client.blindbox import TYPE_BLINDBOX
from .aes import decrypt


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


def handle_pkt(pkt):
    if TCP in pkt:
        print "got a packet"
        # pkt.show2()
        sys.stdout.flush()

        if ('\x00' + bytes(pkt[TCP].payload)[:3]) == struct.pack(">L", TYPE_BLINDBOX):
            print "a BlindBox packet with payload %s" % decrypt(str(pkt[TCP].payload)[3:])
        else:
            print "a TCP packet with payload %s" % decrypt(str(pkt[TCP].payload))


def main():
    ifaces = filter(lambda i: 'eth' in i, os.listdir('/sys/class/net/'))
    iface = ifaces[0]
    print "sniffing on %s" % iface
    sys.stdout.flush()
    sniff(iface=iface,
          prn=lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()
