
n = int(input('몇 개를 출력하시겠습니까? : '))

for i in range (1, n+1) :
    if i%2 != 0 :
        print('+', end='')
    else :
        print('-', end='')    