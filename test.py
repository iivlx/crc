#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Test cases for CRC checksums '''

from crc import crc

check = 0x313233343536373839 # b'123456789'
# Parity
assert crc(check, size=1, poly=1) == 1 # even parity
assert crc(check, size=1, poly=1, xorout=1) == 0 # odd parity
# 3-bit CRC
assert crc(0b11010011101100, size=3, poly=0b1011) == 0b100 # 3-bit wikipedia
# 8-bit CRC
assert crc(check, size=8, poly=0x07) == 0xF4 # CRC-8
assert crc(check, size=8, poly=0x9B, init=0xFF) == 0xDA # CRC-8/CDMA2000
assert crc(check, size=8, poly=0x07, init=0xFF, refin=True, refout=True) == 0xD0 # CRC-8/ROHC
assert crc(check, size=8, poly=0x9B, refin=True, refout=True) == 0x25 # CRC-8/WCDMA
# 16-bit CRC
assert crc(check, size=16, poly=0x8005, refin=True, refout=True) == 0xBB3D # CRC-16/ARC
assert crc(check, size=16, poly=0x0589, xorout=0x0001) == 0x007E # CRC-16/DECT-R
assert crc(check, size=16, poly=0x0589) == 0x007F # CRC-16/DECT-X
assert crc(check, size=16, poly=0x1021, init=0xFFFF, xorout=0xFFFF) == 0xD64E # CRC-16/GENIBUS
# 32-bit CRC
assert crc(check, size=32, poly=0x04C11DB7, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF) == 0xCBF43926  # CRC-32
assert crc(check, size=32, poly=0x814141AB) == 0x3010BF7F # CRC-32Q
assert crc(check, size=32, poly=0x04C11DB7, xorout=0xFFFFFFFF ) == 0x765E7680 # CRC-32/POSIX
assert crc(check, size=32, poly=0x1EDC6F41, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF) == 0xE3069283 # CRC-32C
assert crc(check, size=32, poly=0xA833982B, init=0xFFFFFFFF, refin=True, refout=True, xorout=0xFFFFFFFF) == 0x87315576 # CRC-32D