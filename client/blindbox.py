from scapy.all import Packet, StrFixedLenField, X3BytesField

TYPE_BLINDBOX = 0x811ad8


class BlindBox(Packet):
    name = "BlindBox Packet"
    fields_desc = [
        X3BytesField("protocol", TYPE_BLINDBOX),
        StrFixedLenField("token", "                ", 16)
    ]
