def roots( n ) :
    if n==1 :
        return True
    
    for i in range(1, n//2+1) :
        if(i*i == n) :
            return True
    return False

def solution(left, right):
    
    answer = 0
    for i in range(left, right+1) :
       if(roots( i )) :
           answer -=i
       else :
           answer+=i    
           
    return answer

left = 1
right = 2
c = solution(left, right)
print(c)