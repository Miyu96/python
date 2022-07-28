def multi( n ) :
    
    if n == 1 :
        return 4
    
    for i in range(1, n//2+1) :
        if i*i == n :
            return (i+1)*(i+1)
    
    return -1

n = int(input('정수를 입력해주세요 : '))

print(multi(n))
