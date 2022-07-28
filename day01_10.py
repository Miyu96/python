n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요? : '))

for i in range(n//w) :
    print('*'*w)

nokori = n%w

print('*'*nokori)

   