import random


def choose_option():
  options = ('piedra', 'papel', 'tijera')

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('Esa opcion no es valida')
    return None, None

  computer_option = random.choice(options)

  print('-' * 10)
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, users_wins, computer_wins):

  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera.')
      print('User gana!')
      users_wins += 1
    else:
      print('Papel gana a piedra')
      print('Computer gana!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra.')
      print('User gana!')
      users_wins += 1
    else:
      print('Tijera gana a papel.')
      print('Computer gana!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel.')
      print('User gana!')
      users_wins += 1
    else:
      print('Piedra gana a tijera.')
      print('Computer gana!')
      computer_wins += 1
  return users_wins, computer_wins


def run_game():
  rounds = 1
  computer_wins = 0
  users_wins = 0

  while True:
    print('*' * 20)
    print('ROUND ', rounds)
    print('-' * 10)

    # Funcion de asignar valores a jugador y maquina
    user_option, computer_option = choose_option()

    print('-' * 10)

    # Chequea las reglas del juego
    users_wins, computer_wins = check_rules(user_option, computer_option,
                                            users_wins, computer_wins)

    print('-' * 10)
    print('user wins ==> ', users_wins)
    print('computer wins ==> ', computer_wins)

    if computer_wins == 2:
      break
    if users_wins == 2:
      break
    rounds += 1


run_game()
