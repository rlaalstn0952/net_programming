import socket
import struct
import binascii

class Udphdr:
    def __init__(self, SrcPort, DstPort, Length, Checksum):
        self.SrcPort = SrcPort
        self.DstPort = DstPort
        self.Length = Length
        self.Checksum=Checksum

    def pack_Udphdr(self):
        packed=b''
        packed += struct.pack('!4H', self.SrcPort, self.DstPort, self.Length, self.Checksum)

        return packed




def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:8])
    return unpacked

def getSrcPort(unpacked_Udpheader):
    return unpacked_Udpheader[0]

def getDstPort(unpacked_Udpheader):
    return unpacked_Udpheader[1]

def getLength(unpacked_Udpheader):
    return unpacked_Udpheader[2]

def getChecksum(unpacked_Udpheader):
    return unpacked_Udpheader[3]

ip = Udphdr(5555,80, 1000, 0xFFFF)
packed_Udphdr = ip.pack_Udphdr()

unpacked_Udphdr = unpack_Udphdr(packed_Udphdr)


print(binascii.b2a_hex(packed_Udphdr))
print(unpacked_Udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{} '\
    .format(getSrcPort(unpacked_Udphdr), getDstPort(unpacked_Udphdr),getLength(unpacked_Udphdr), getChecksum(unpacked_Udphdr)))