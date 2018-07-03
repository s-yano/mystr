# -*- coding: utf-8 -*-

from _mystr import ffi, lib

def to_upper(s0):
    s = ffi.new('char[]', s0.encode('ascii'))
    lib.to_upper(s)
    return ffi.string(s).decode('ascii')

def main():
    print(to_upper(input()))
