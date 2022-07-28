def med3(a,b,c) :
    
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b<c:
        return b
    else:
        return c
    

a = int(input('입력1 : '))
b = int(input('입력2 : '))    
c = int(input('입력3 : '))

print(f'중앙값은 {med3(a,b,c)}입니다.')
            