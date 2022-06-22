def computador_escolhe_jogada(n,m):
    jogada_pc=1
    while jogada_pc!=m:
        if(n-jogada_pc)%(m+1)==0:
            return jogada_pc
        else:
            jogada_pc+=1
    return jogada_pc
          
def usuario_escolhe_jogada(n,m):
    jogada_valida=False
    while not jogada_valida:
        jogada_human=int(input('Quantas peças você vai tirar?'))
        if jogada_human>m or jogada_human<1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            jogada_valida=True
    return jogada_human

def partida():
    n=int(input('Quantas peças?'))
    m=int(input('Limite de peças por jogada?'))  
    vez_pc=False
    if n<=0 or m<=0:
        print('Não é possível iniciar o jogo com',n,'e',m,'número de peças!')
        partida()
    if n%(m+1)==0:
        print()
        print('Você começa!')
    else:
        print()
        print('Computador começa!')
        vez_pc=True
    while n>0:
        if vez_pc:
            jogada_pc=computador_escolhe_jogada(n,m)
            n=n-jogada_pc
            print()
            print('O computador tirou',jogada_pc,'peça(s).')
            print('Agora restam',n,'peça(s) no tabuleiro.')
            print()
            vez_pc=False
        else:
            jogada_human=usuario_escolhe_jogada(n,m)
            n=n-jogada_human
            print()
            print('Você tirou',jogada_human,'peça(s).')
            print('Agora restam',n,'peça(s) no tabuleiro.')
            print()
            vez_pc=True
    print('Fim do jogo! O computador ganhou!')
    sair()

def campeonato():
    rodada=1
    while rodada<=3:
        print()
        print('**** Rodada', rodada, '****')
        print()
        partida()
        sair()
        rodada+=1
    print()
    print('Placar: Você 0 x 3 Computador')
     
def sair():
    print()
    print('Selecione uma opção:')
    print()
    print('1 - para escolher novo modo de jogo')
    print('2 - para sair')

    select_sair=input('Selecione uma opção:')
    if select_sair=='1':
        jogo()
    if select_sair=='2':
        exit()
   
def jogo():
    print()
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato')
    print()
    select_jogo=input('Qual modo deseja jogar?')
    if select_jogo=='1':
        print('Você escolheu uma partida isolada!')
        partida()
    if select_jogo=='2':
        print('Voce escolheu um campeonato!')
        campeonato()
    else:
        print('Digite uma opçao válida!')
        jogo()

jogo()
