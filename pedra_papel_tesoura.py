# Blibiotecas

import random


# Funcao que escolhe o numero para o "robo"
def robo():
    escolha_robo = random.randint(1, 3)
    return escolha_robo


# Funcao que verifica quem ganhou
def identificar_ganhador(escolhido_player, escolhido_robo):
    player_ganha = bool
    # //// 1 = pedra, 2 = papel, 3 = tesoura ////
    # Quem ganha:
    if escolhido_player == 1 and escolhido_robo == 2:
        player_ganha = False
    if escolhido_player == 1 and escolhido_robo == 3:
        player_ganha = True
    if escolhido_player == 2 and escolhido_robo == 1:
        player_ganha = True
    if escolhido_player == 2 and escolhido_robo == 3:
        player_ganha = False
    if escolhido_player == 3 and escolhido_robo == 2:
        player_ganha = True
    if escolhido_robo == 1 and escolhido_player == 3:
        player_ganha = False
    return player_ganha


# Funcao em que o player escolhe entre ppt, etc.
def escolha_do_player(loop):
    numero_player = int
    while loop:
        try:
            numero_player = int(input("Digite o que voce escolheu: "))
            loop = False
        except ValueError:
            print("Digite um numero corretamente!")
            loop = True
    return numero_player


# Funcao que identifica quem ganhou
def identificador_ganhador(var_player, escolha_do_robo, escolha_player):
    # "Convertor de [1, 3, 3] para ppt"
    escolha_do_robo_convertido = str
    if escolha_do_robo == 1:
        escolha_do_robo_convertido = "pedra"
    if escolha_do_robo == 2:
        escolha_do_robo_convertido = "papel"
    if escolha_do_robo == 3:
        escolha_do_robo_convertido = "tesoura"
    # Quando ha um empate
    if escolha_do_robo == escolha_player:
        print("Ouve um empate!\nO 'robo' escolheu {}!".format(escolha_do_robo_convertido))
    # Quando o player ganha
    if var_player == True:
        print("Voce ganhou!")
        print("O 'robo' escolheu {}!".format(escolha_do_robo_convertido))
    # Quando o robo ganha
    if not var_player:
        print("Voce perdeu ;(")
        print("O 'robo' escolheu {}!".format(escolha_do_robo_convertido))


# Boas vindas

print("Ola! Seja bem vindo(a) ao pedra, papel ou tesoura!")
print("Para comecar, digite o numero de acordo com o que voce quer usar.")

# Variaveis
vezes = 0

loop = True

# Chamar funcao
while True:
    input("[Aperte ENTER]")
    print("Pedra[1]\nPapel[2]\nTesoura[3]")
    escolha_robo = robo()
    numero_player = escolha_do_player(loop)
    player_ganha = identificar_ganhador(numero_player, escolha_robo)
    identificador_ganhador(player_ganha, escolha_robo, numero_player)
