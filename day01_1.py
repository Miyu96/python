# -*- coding: utf-8 -*-
def f(a,b,c,d):

    maximum = a

    if b>maximum:
        maximum = b
    
    if c>maximum:
        maximum = c

    if d>maximum:
        maximum = d

    return maximum

a = int(input('정수 a의 값? : '))
b = int(input('정수 b의 값? : '))
c = int(input('정수 c의 값? : '))
d = int(input('정수 d의 값? : '))


maximum= f(a,b,c,d);
print(f'최대값은 {maximum}입니다')