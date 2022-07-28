a = int(input('정수를 입력해주세요 : '))

b = a
i = 0
while True :
    num1 = a//10 + a%10
    a = (a%10)*10 + num1%10
    i+=1
    if(a == b) :
        print(i)
        break

    
        