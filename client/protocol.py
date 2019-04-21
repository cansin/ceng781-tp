from scapy.all import Packet, StrFixedLenField


class BlindBox(Packet):
    name = "BlindBox"
    fields_desc = [StrFixedLenField("token", "                ", 16)]
