#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' CRC calculations

'''

from reflect import reflect, reflectbin

def crcinit(init, size, poly):
    highbit = 1 << size-1
    for i in range(init.bit_length()):
        bit = init & 1
        if bit:
            init = init ^ poly
        init = init >> 1
        if bit:
            init |= highbit
    return init
    
def crc(data, size=0, poly=0, refin=0, refout=0, init=0, direct=1, xorout=0):
    ''' calculate a CRC checksum of a given size
    bitwise implementation
    '''
    if refin:
        data = reflect(data)
    if init:
        if direct:
            init = crcinit(init, size, poly)
        pad_bits = data.bit_length() % 4
        data = (init << data.bit_length()+pad_bits) + data
    data = data << size
    out = 0
    length = data.bit_length()
    for i in range(length):
        next = (data >> (length-i)-1) & 1
        out = out << 1
        out |= next
        if out >> size:
            out ^= poly
        out &= (1 << size) - 1
    if refout:
        out = reflectbin(out, size)
    return out ^ xorout

if __name__ == '__main__':
    import test