#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Reflect the bits in a byte '''

def reflectbin(b, length):
    return int( bin(b)[2:].zfill(length)[::-1], 2)

def reflectbyte(byte):
    return int( bin(byte)[2:].zfill(8)[::-1], 2)

def reflectbytes(b):
    r = bytes()
    for byte in b:
        r += reflectbyte(byte).to_bytes(1,'big')
    return r

def reflect(num):
    ''' reflect the bits in each byte of a number '''
    s = hex(num)[2:]
    if len(s) % 2:
        s = '0' + s
    return int.from_bytes(reflectbytes(bytes.fromhex(s)), 'big')