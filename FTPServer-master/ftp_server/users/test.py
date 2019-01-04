# -*- coding: UTF-8 -*-
import os,sys
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path.append(DIR))

print(sys.path)
