#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO('你看过了许多美景,\n你看过了许多美女')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
