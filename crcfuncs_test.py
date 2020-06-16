#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Test cases for CRC functions '''

from crcfuncs import *

check = 0x313233343536373839

assert crc8(check) == 0xF4
assert crc8cdma2000(check) == 0xDA
assert crc8rohc(check) == 0xD0
assert crc8wcdma(check) == 0x25
# 16-bit CRC
assert crc16arc(check) == 0xBB3D
assert crc16dectr(check) == 0x007E
assert crc16dectx(check) == 0x007F
assert crc16genibus(check) == 0xD64E
# 32-bit CRC
assert crc32(check) == 0xCBF43926
assert crc32q(check) == 0x3010BF7F
assert crc32posix(check) == 0x765E7680
assert crc32c(check) == 0xE3069283
assert crc32d(check) == 0x87315576
# 64-bit CRC
assert crc64(check) == 0x995DC9BBDF1939FA