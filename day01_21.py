def check( n ) :
    n_str = str(n)
    le = len(n_str)
    num1 = 0
    num2 = 0
    
    for i in range(le) :
        if i<le//2 :
            num1+=int(n_str[i])
        else :
            num2+=int(n_str[i])    

    if num1 == num2 :
        print('LUCKY')
    else :
        print('READY')    

n = int(input('정수를 입력해주세요 : '))
check(n)