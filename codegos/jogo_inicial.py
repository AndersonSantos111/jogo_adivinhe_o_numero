import random



def gerarNumero():
    return random.randint(0, 20)

def pedirEntrada():
    entrada = input('Chute um número (ou digite "pare" para encerrar): ').strip()
    return entrada



limite_chances = 3      ## chances por rodada
limite_rodadas = 5      ## número maximo de rodadas
rodada_atual = 1        ## começa na rodada 1

numero = gerarNumero()
chances_restantes = limite_chances

while rodada_atual <= limite_rodadas:

    print(f"Rodada {rodada_atual} de {limite_rodadas}")
    print(f"Chances restantes: {chances_restantes}")

    entrada = pedirEntrada()

 
    if entrada.lower() == "pare":
        print("Jogo encerrado pelo usuário.")
        break

   
    if entrada == "":
        print("Você não digitou nada.")
        continue

    if not entrada.isdigit():
        print("Digite apenas números!")
        continue

    NumeroUsuario = int(entrada)

    if NumeroUsuario > numero:
        print(f"É menor que {NumeroUsuario}")
        chances_restantes -= 1

    elif NumeroUsuario < numero:
        print(f"É maior que {NumeroUsuario}")
        chances_restantes -= 1

    else:
        print("Acertou seu cabeçudo")
       
        numero = gerarNumero()
        chances_restantes = limite_chances
       
        rodada_atual += 1
        continue

    
    if chances_restantes == 0:
        print(f"\n cabosse! O número era {numero}.")
    
        chances_restantes = limite_chances
        numero = gerarNumero()
        rodada_atual += 1

print("\nGAME OVER!")
