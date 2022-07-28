

area = int(input('넓이 A : '))


i = 1
for i in range (1, area+1) :
    if (area % i) != 0 :
        i+=1
        continue
    
    print(f'{i} X {area//i}')
    
    i+=1