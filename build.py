# -*- coding: utf-8 -*-

import cffi

ffi = cffi.FFI()
ffi.cdef('''
  void to_upper(char *s);
''')
ffi.set_source('_mystr', open('c/mystr.c').read())
ffi.compile()
