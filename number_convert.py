Arabic=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
Roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
Key={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def Arabic2Roman():
    print('Enter your number under 3999')
    number=int(input())
    answer=''
    i=0
    #поскольку римские числа свыше 3999 нельзя вывести на экран без спец. символов, вводим проверку
    if number>3999 or number<=0:
        print ('Error. Write corect number')
    else:
        while number>0:
            #проверяем разряды введеного числа и их количество 
            while Arabic[i]<=number:
                answer=answer+Roman[i]
                number=number-Arabic[i]
            i+=1
    print(answer)

def Roman2Arabic():
    print('Enter your number')
    number=input()
    answer = 0
    for i in range(len(number)):
         # поскольку не удается избавится от ошибки, вводим исключение
         try:
             # по значениям ключей сравниваем соседние символы введеного числа
             if Key[number[i]]<Key[number[i+1]]:
                 answer=answer-[number[i]]
             else:
                 answer=answer+Key[number[i]]
         except IndexError:
                 answer=answer+Key[number[i]]
    print(answer)

print('Press 1 if you want convert Arabic to Roman. Press 2 if you want convert Roman to Arabic')
result=int(input())
if result==1:
    Arabic2Roman()
elif result==2:
    Roman2Arabic()
else:
    print('Wrong number')
    
    


