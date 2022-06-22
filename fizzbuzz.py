input_numero=int(input('Digite um número inteiro: '))

if input_numero%3==0 or input_numero%5==0:
    print('FizzBuzz')
else:
    print(input_numero)