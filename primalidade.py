input_num=int(input('Digite um número inteiro positivo: '))
first_prime_num=2
if (input_num%first_prime_num==0 and input_num!=first_prime_num) or input_num==1:
    print('Não Primo')
else:
    print('Primo')