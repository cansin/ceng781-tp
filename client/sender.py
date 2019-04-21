import random
import socket
import sys

from scapy.all import Ether
from scapy.all import sendp, get_if_list, get_if_hwaddr
from scapy.layers.inet import IP, TCP

from .aes import encrypt
from .protocol import BlindBox


def get_if():
    ifs = get_if_list()
    iface = None  # "h1-eth0"
    for i in ifs:
        if "eth0" in i:
            iface = i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface


def main():
    print sys.argv

    if len(sys.argv) < 2:
        print 'pass 1 argument: "<message>"'
        exit(1)

    addr = socket.gethostbyname("10.0.2.2")
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt / IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152, 65535)) / BlindBox(
        token=encrypt(sys.argv[1])) / encrypt(sys.argv[1])
    pkt.show2()
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
