def electricPay( elec ) :
    
    total = 0
    
    if elec<100 :
       total = 410+60.7*elec
    elif elec>=100 and elec<=200  :
        total = 910 + 60.7*100 + 125.9*(elec-100)
    else : 
        total = 1600 + 60.7*100 + 125.9*100+ 187.9*(elec-200)
    total *= 1.137
    return total

elec = int(input('전기 사용량을 입력해주세요 : '))
print(f'전기사용금액 : {int(electricPay( elec ))}')