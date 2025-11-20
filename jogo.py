import random
import os

# VARIAVEIS:
limite_chances = 3      ## chances por rodada
limite_rodadas = 5      ## número maximo de rodadas
# rodada_atual = 1        ## começa na rodada 1

tabela_pontos = {'chaces_restantes': limite_chances, 'rodada_atual': 0, 'pontuação': 0}

# FUNCOES:
def gerarNumero(): # Solteia um numero
    return random.randint(0, 10)

numero = gerarNumero() # Recolhe o numero sorteado 

def pedirEntrada(): # Recolhendo entrada do player
    entrada = input('Chute um número (ou digite "pare" para encerrar): ').strip()
    return entrada

def atualizar_tabela(NumeroUsuario, N): # Atualiza dados da tabela
    os.system('cls')
    if NumeroUsuario > N: # Checagem de acertos
        print(f"É menor que {NumeroUsuario}")
        #chances_restantes -= 1
        tabela_pontos["chaces_restantes"] -= 1

    elif NumeroUsuario < N:
        # chances_restantes -= 1
        tabela_pontos["chaces_restantes"] -= 1
        

    else:
        print("Acertou seu cabeçudo")
       
        # numero = gerarNumero()
        # print(numero)
        if tabela_pontos["chaces_restantes"] == 3:
            tabela_pontos["pontuação"] += 3

        if tabela_pontos["chaces_restantes"] == 2:
            tabela_pontos["pontuação"] += 2

        if tabela_pontos["chaces_restantes"] == 1:
            tabela_pontos["pontuação"] += 1

        tabela_pontos["chaces_restantes"] = limite_chances
       
        tabela_pontos["rodada_atual"] += 1
        return True










# GAME:

while tabela_pontos["rodada_atual"] <= limite_rodadas:

    # print(f"|Rodada {rodada_atual} de {limite_rodadas}|")
    # print(f"|Chances restantes: {chances_restantes}|")
    print(tabela_pontos)

    entrada = pedirEntrada()

 
    if entrada.lower() == "pare": # Encerra o jogo
        os.system('cls')
        print("Jogo encerrado pelo usuário.")
        break

   
    if entrada == "": # Checa se digiotou algo
        os.system('cls')
        print("Você não digitou nada.")
        continue

    if not entrada.isdigit(): # Checa se digitou um número
        os.system('cls')
        print("Digite apenas números!")
        continue

    if(atualizar_tabela(int(entrada), numero)): # Atualizar tabela
        continue

    
    if tabela_pontos["chaces_restantes"] == 0:
        os.system('cls')
        print(f"\n cabosse! O número era {numero}.")
    
        tabela_pontos["chaces_restantes"] = limite_chances
        numero = gerarNumero()
        tabela_pontos["rodada_atual"] += 1

print("\nGAME OVER!")
