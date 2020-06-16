#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Test cases for CRC checksums '''

from crc import crc

check = 0x313233343536373839 # b'123456789'

# 8-bit CRC
assert crc(check, size=8, poly=0x07) == 0xF4 # CRC-8
assert crc(check, size=8, poly=0x9B, init=0xFF) == 0xDA #CRC-8/CDMA2000
# 16-bit CRC
assert crc(check, size=16, poly=0x8005, refin=True, refout=True) == 0xBB3D # CRC-16/ARC
assert crc(check, size=16, poly=0x0589, xorout=0x0001) == 0x007E # CRC-16/DECT-R
assert crc(check, size=16, poly=0x0589) == 0x007F # CRC-16/DECT-X
assert crc(check, size=16, poly=0x1021, init=0xFFFF, xorout=0xFFFF) == 0x541A  # CRC-16/GENIBUS
# 32-bit CRC
assert crc(check2, size=32, poly=0x04C11DB7, init=0xFFFFFFFF, xorout=0xFFFFFFFF) == 0xFED55B05  # CRC-32
assert crc(check, size=32, poly=0x814141AB) == 0x3010BF7F # CRC-32Q
assert crc(check, size=32, poly=0x04C11DB7, xorout=0xFFFFFFFF ) == 0x765E7680 # CRC-32/POSIX