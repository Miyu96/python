a = int(input('정수 a : '))
b = int(input('정수 b : '))

if(a>b) :
    a,b = b,a

sum = 0

for i in range(a , b+1) :
    sum+=i
    

print(sum)    