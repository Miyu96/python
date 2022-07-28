
a = int(input("정수 a의 값을 입력해주세요 : "))
b = int(input("정수 b의 값을 입력해주세요 : "))

if(a>b) :
    a,b = b,a

sum = 0
for i in range(a, b+1) :
    
    if(i<b) :
        print(f'{i}+', end='')
        sum+=i


sum += b
print(f'{b}={sum}')   