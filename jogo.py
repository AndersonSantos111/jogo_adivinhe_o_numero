import random

rodada = 3

def gerarNumero ():
    numero = random.randint(0, 20)
    return numero

numero = gerarNumero()

while True:
    NumeroUsuario = int(input('Chute um número: ').strip())
    if not NumeroUsuario:
        print('Você não digitou nada ainda')
    else:
        if NumeroUsuario > numero:
            print(f'é menor que {NumeroUsuario}')
        elif NumeroUsuario < numero:
            print(f'é maior que {NumeroUsuario}')
        else:
            print('Acertou!')
            numero = gerarNumero()