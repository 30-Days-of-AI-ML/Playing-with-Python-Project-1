# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:23:52 2020
@author: Gyan Krishna

install the mathparse library:-
pip install mathparse
"""

from mathparse import mathparse
print("math parse demonstration")

ans = mathparse.parse('50 * (90 / 29) + 2')
number = mathparse.parse('ten * nine', language='ENG')
ans2 = mathparse.parse("49 plus eight plus 10", language="ENG")

print(ans2)
print(number)
print(ans)
