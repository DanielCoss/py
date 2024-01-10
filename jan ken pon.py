import random

def choice(input):
    if input == 1:
        return 'Piedra'
    elif input == 2:
        return 'Papel'
    elif input == 3:
        return 'Tijeras'
    else:
        return 'N/A'

def text(user_option, auto_option):
    print(f'Jugador eligio {choice(user_option)}')
    print(f'Computador eligio {choice(auto_option)}')
    
def user_input():
    flag = False
    while flag == False:
        user_option = input('1 para piedra, 2 para papel o 3 para tijera => ')
        if (user_option.isdigit()) : 
            user_option = int(user_option)
            break
        print("Solo usa 1, 2, 3 como respuesta!")
    return user_option

def pc_option():
    auto_option = random.randint(1,3)
    return auto_option

def winner(player1_option, player2_option, player1_name, player2_name):
    if player1_option == player2_option:
        return 'Empate'
    elif (player1_option == 3 and player2_option == 2) or (player1_option == 2 and player2_option == 1) or (player1_option == 1 and player2_option == 3): 
        return player1_name
    else:
        return player2_name

def main():
    user = user_input()
    pc = pc_option()
    text(user, pc)
    print(f'Resultado => {winner(user, pc, "Jugador", "Computador")}')

main()