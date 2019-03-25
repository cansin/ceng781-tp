from scapy.all import Packet, StrFixedLenField

class DPIP(Packet):
    name = "Blind"
    fields_desc = [ StrFixedLenField("token", "                ", 16) ]