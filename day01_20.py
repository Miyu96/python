data = input('숫자로 이루어진 문자열을 입력하세요. ')
result = int(data[0])

for i in range(1, len(data)) :
    num = int(data[i])
    if result ==0 or num ==0 or num ==1 :
        result+=num
    else : 
        result*= num 
        
print(result)         
