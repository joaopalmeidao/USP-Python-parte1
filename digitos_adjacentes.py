input_num=int(input('Digite um número inteiro: '))
num1=input_num
rest1=input_num%10
while input_num//10!=0:
    input_num=input_num//10
    rest=input_num%10
    if rest==rest1:
        print('sim')
        input_num=num1
        break
    rest1=rest
if input_num//10==0:
    print('não')
