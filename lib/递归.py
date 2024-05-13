#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/9 9:31
# Author    : weixinlan
# @File     : 递归.py
# @Software : PyCharm
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))