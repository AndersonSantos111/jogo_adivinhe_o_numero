import random
import os

# VARIAVEIS:
limite_chances = 3      ## chances por rodada
limite_rodadas = 5      ## número maximo de rodadas

tabela_pontos = {'chaces_restantes': limite_chances, 'rodada_atual': 0, 'pontuação': 0}

# HISTÓRICO:
historico = []  # registra vitorias e derrotas

# DIFICULDADE:
dificuldade_bonus = 0  # aumenta +5 a cada 2 rodadas

# FUNCOES:
def gerarNumero(): # Solteia um numero
    return random.randint(0, 10 + dificuldade_bonus)

numero = gerarNumero() # Recolhe o numero sorteado 

def pedirEntrada(): # Recolhendo entrada do player
    entrada = input('Chute um número (ou digite "pare" para encerrar): ').strip()
    return entrada

def atualizar_tabela(NumeroUsuario, N): # Atualiza dados da tabela
    os.system('cls')
    if NumeroUsuario > N: # Checagem de acertos
        print(f"É menor que {NumeroUsuario}")
        tabela_pontos["chaces_restantes"] -= 1

    elif NumeroUsuario < N:
        print(f"É maior que {NumeroUsuario}")
        tabela_pontos["chaces_restantes"] -= 1
        

    else:
        print("Acertou seu cabeçudo")

        # -registrar vitória -
        pontos_ganhos = 3 if tabela_pontos["chaces_restantes"] == 3 else \
                        2 if tabela_pontos["chaces_restantes"] == 2 else \
                        1
        historico.append({
            "rodada": tabela_pontos["rodada_atual"] + 1,
            "resultado": "VITÓRIA",
            "numero_sorteado": N,
            "chute": NumeroUsuario,
            "pontos_ganhos": pontos_ganhos
        })
      

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

        #  aumenta a difilcuade a cada 2 rodadas
        if tabela_pontos["rodada_atual"] % 2 == 0:
            dificuldade_bonus += 5
            print(f"\n ih boyzin... agora a chapa esquentou: agora o intervalo é de 0 até {10 + dificuldade_bonus} ")
       
        numero = gerarNumero()
        continue

    
    if tabela_pontos["chaces_restantes"] == 0:
        os.system('cls')
        print(f"\n cabosse! O número era {numero}.")
    
        # -registrar derrota-
        historico.append({
            "rodada": tabela_pontos["rodada_atual"] + 1,
            "resultado": "DERROTA",
            "numero_sorteado": numero,
            "chute": int(entrada),
            "pontos_ganhos": 0
        })
        

        tabela_pontos["chaces_restantes"] = limite_chances

        # ---- AUMENTO DE DIFICULDADE A CADA 2 RODADAS ----
        if tabela_pontos["rodada_atual"] % 2 == 0:
            dificuldade_bonus += 5
            print(f"\n ih boyzin... agora a chapa esquentou: intervalo é de 0 até  {10 + dificuldade_bonus} ")
        # --------------------------------------------------

        numero = gerarNumero()
        tabela_pontos["rodada_atual"] += 1

print("\nGAME OVER!")

#  HISTÓRICO 
print("\n= HISTÓRICO DE RODADAS =")
for i, h in enumerate(historico, start=1):
    print(
        f"{i:02d} | Rodada {h['rodada']} | {h['resultado']} | "
        f"Sorteado: {h['numero_sorteado']} | Chute: {h['chute']} | Pontos: {h['pontos_ganhos']}"
    )
