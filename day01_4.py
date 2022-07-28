def waterPay(cm, wl) :
    
    watercnt = 0
    if cm =='A':
        watercnt = wl*100
    elif cm=='B' :
        if wl<=50 :
            watercnt = wl*150
        else :
            watercnt = 150*50 + (wl-50)*75
    
    else :
        print('옳바른 회사명을 입력해주세요.')
        return 0
    return watercnt

cm = input('회사명을 입력해주세요 : ')
wl = int(input('물의 사용량을 입력해주세요 : '))

print(f'사용요금 : {waterPay(cm, wl)}원')