def sum( n ):

    sum = 0
    for i in range(1, n+1) :
        sum+=i
        print(i)
    return sum


n = int(input('정수 : '))
print(sum(n))        
        
    
    