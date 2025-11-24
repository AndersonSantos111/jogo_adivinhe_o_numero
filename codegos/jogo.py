import random
import os

# VARIAVEIS
limite_chances = 3      ## chances por rodada 
limite_rodadas = 999     ## número maximo aumentei para 999 para assim o jogo rodar por mais tempo

tabela_pontos = {'chaces_restantes': limite_chances, 'rodada_atual': 1, 'pontuação': 0, 'nivel': 1}

# HISTÓRICO:
historico = []  # registra vitorias e derrotas

# DIFICULDADE:
dificuldade_bonus = 0  # aumenta +5 a cada 2 rodadas

#CARREGAR_SAVE
def carregar_save():
    escolha = input("Deseja carregar o save anterior? (s/n): ").strip().lower()
    if escolha == 'n':
        return None
    if os.path.exists("salvamento.txt"): #o carregamento só ocorre se o arquivo existir e se confirmado
        with open("salvamento.txt", "r") as save:
            linhas = save.readlines()
        dados = {}
        for linha in linhas:
            linha = linha.strip()
            if "=" in linha:
                chave, valor = linha.split("=")
                dados[chave] = int(valor)
            print("Save carregado")
        return dados
    else:
        print("Nenhum save encontrado")
        return None

    

# FUNCOES:
def gerarNumero(): # Sorteia um numero
    return random.randint(0, 10 + dificuldade_bonus)

numero = gerarNumero() # Recolhe o numero sorteado 

def pedirEntrada(): # Recolhendo entrada do player
    entrada = input('Chute um número (ou digite "pare" para encerrar): ').strip()
    return entrada

def dica(nivel, estado, entrada): # verifica o nivel e da uma dica de acordo com o nivel
    if estado == 'maior':
        if nivel == 1:
            print(f"É menor que {entrada}")
    elif estado == 'menor':
        if nivel == 1:
            print(f"É maior que {entrada}")
        # if nivel == 2:
        #     n1 = random.randint(entrada - (entrada-1),(entrada -1))
        #     n1 = numero - n1
        #     print(f'É maior que a soma entre {n1} + {n2} {entrada}')



def atualizar_tabela(NumeroUsuario, N): # Atualiza dados da tabela
    os.system('cls')
    if NumeroUsuario > N: # Checagem de acertos
        dica(tabela_pontos["nivel"], 'maior', NumeroUsuario)
        tabela_pontos["chaces_restantes"] -= 1

    elif NumeroUsuario < N:
        dica(tabela_pontos["nivel"], 'menor', NumeroUsuario)
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

dados = carregar_save()
if dados is not None:
    tabela_pontos.update(dados)
    tabela_pontos.update({k: v for k, v in dados.items() if k in tabela_pontos})
    print("Save aplicado com sucesso!")
else:
    print("Iniciando novo jogo...")


if dados is not None and "dificuldade_bonus" in dados:
    dificuldade_bonus = dados["dificuldade_bonus"]




while tabela_pontos["rodada_atual"] <= limite_rodadas:

    print(
        f"Rodada: {tabela_pontos['rodada_atual']} | "
        f"Chances: {tabela_pontos['chaces_restantes']} | "        #mudei para que  a tabela de pontos fique mais bonita
        f"Pontos: {tabela_pontos['pontuação']} | "
        f"Nível: {tabela_pontos['nivel']}"
    ) 

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

    if entrada == 0:
        print('Não pode ser zero!')
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

# SALVAMENTO DO HISTÓRICO EM ARQUIVO
with open("salvamento.txt", "w") as save:
    for chave, valor in tabela_pontos.items():
        save.write(f"{chave}={valor}\n")
    save.write(f"dificuldade_bonus={dificuldade_bonus}\n")
    
    print("\nProgresso salvo em 'salvamento.txt'.")
   