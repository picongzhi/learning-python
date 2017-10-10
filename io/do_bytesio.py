#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

data = '隔着玻璃窗，我早已沉醉在蓝色的街'.encode('utf-8')
f = BytesIO(data)
print(f.read())
