def ro(n) :
    root = 0
    pwr = 0
    for i in range(2, n//2+1) :
        mul = 1
        for j in range(1, 6) :
            mul *=i
            if( mul == n ) :
                root = i
                pwr = j
                break
        if( root != 0) :
            print(f'root : {root}, pwr : {pwr}')   
            break
        else :
            print('알맞은 값이 없습니다.')
            break
     
        
n = int(input('정수를 입력해주세요 : '))
ro(n)