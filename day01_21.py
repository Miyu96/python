def check( n ) :
    length = len(str(n))
    num1 = 0
    num2 = 0
    
    for i in range(length) :
        if i<length//2 :
            num1+=n[i]
        else :
            num2+=n[i]    

    if num1 == num2 :
        print('Lucky')
    else :
        print('READY')    

n = int(input('정수를 입력해주세요 : '))
check(n)