# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:01:36 2022

@author: user
"""
def add(n1,n2,cb):
	cb(n1+n2)
def handle1(result):
	print("結果是",result)
def handle2(result):
	print("Result of Add is",result)

add(3,4,handle1) # 結果是 7 流程 add呼叫handle1（函式）然後再計算n1+n2
add(5,6,handle2) # Result of Add is 11
