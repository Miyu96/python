a = int(input('정수를 입력해주세요 : '))
b = int(input('정수를 입력해주세요 : '))

if a>b :
    a,b = b,a
    
max = 0   
for i in range(1, b//2+1) :
    if a%i ==0 and b%i ==0 :
        max = i
        continue
    
print(f'최대 공약수 : {max}') 
print(f'최소 공배수 : {a*b//max}')   