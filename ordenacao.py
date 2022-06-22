input_numero1=int(input('Digite o primeiro número inteiro: '))
input_numero2=int(input('Digite o segundo número inteiro: '))
input_numero3=int(input('Digite o terceiro número inteiro: '))

if input_numero3>input_numero2 and input_numero2>input_numero1:
    print('crescente')
else:
    print('não está na ordem crescente')