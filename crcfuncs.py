from crc import crc

crc8 = lambda data: crc(data, size=8, poly=0x07)
crc8cdma2000 = lambda data: crc(data, size=8, poly=0x9B, init=0xFF)
crc8rohc = lambda data: crc(data, size=8, poly=0x07, init=0xFF, refin=True, refout=True)
crc8wcdma = lambda data: crc(data, size=8, poly=0x9B, refin=True, refout=True)
# 16-bit CRC
crc16arc = lambda data: crc(data, size=16, poly=0x8005, refin=True, refout=True)
crc16dectr = lambda data: crc(data, size=16, poly=0x0589, xorout=0x0001)
crc16dectx = lambda data: crc(data, size=16, poly=0x0589)
crc16genibus = lambda data: crc(data, size=16, poly=0x1021, init=0xFFFF, xorout=0xFFFF)
# 32-bit CRC
crc32 = lambda data: crc(data, size=32, poly=0x04C11DB7, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF)
crc32q = lambda data: crc(data, size=32, poly=0x814141AB)
crc32posix = lambda data: crc(data, size=32, poly=0x04C11DB7, xorout=0xFFFFFFFF )
crc32c = lambda data: crc(data, size=32, poly=0x1EDC6F41, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF)
crc32d = lambda data: crc(data, size=32, poly=0xA833982B, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF)
# 64-bit CRC
crc64 = lambda data: crc(data, size=64, poly=0x42F0E1EBA9EA3693, init=0xFFFFFFFFFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFFFFFFFFFF)