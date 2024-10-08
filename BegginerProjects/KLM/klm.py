import os
from time import sleep

# Tempos KLM
H = 0.4  # Hover to Keyboard/Mouse
P = 1.1  # Pointer
K = 0.2  # Click
M = 1.35 # Mentality
R = 2    # Respond time

# Dicionário para os tempos de cada ação - key: value
klm_times = {
    'H': H,
    'P': P,
    'K': K,
    'M': M,
    'R': R
}

# Opções que podem ser escolhidas - key: value
opcoes_disponiveis = {
    1: 'Título',
    2: 'Categoria',
    3: 'Informação Adicional',
    4: 'Descrição',
    5: 'Fotos',
    6: 'Contacto'
}

# Armazena o tempo calculado para cada opção - key: value
test_timer = {
    'Título': 0,
    'Categoria': 0,
    'Informação Adicional': 0,
    'Descrição': 0,
    'Fotos': 0,
    'Contacto': 0
}


# Limpar terminal
def clear_screen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')


# Escolhar opção
def user_input():
  choices = list(opcoes_disponiveis.keys()) + [0, 7]
  try:
    while True:
      option = int(input('Escolha uma opção: '))
      if option in choices:
        return option
      else:
        print(f'Opção inválida {option}! Por favor, tente outra vez.')
  except ValueError:
    print(f'Número inválido {option}! Por favor, tente outra vez.')


# Calcular o tempo para a opcao
def calculate_timer(option):
  if option in opcoes_disponiveis:
    print('H: Hover to Keyboard/Mouse ')
    print('P: Pointer ')
    print('K: Click ')
    print('M: Mentality ')
    print('R: Respond time \n')
    print(f'Insira a sequência de ações KLM para {opcoes_disponiveis[option]}: ', end='')
    klm_input = input().upper()
    tempo_total = 0
    for action in klm_input:
      if action in klm_times:
        tempo_total += klm_times[action]
      else:
        print(f'Opção inválida: {action}')
    test_timer[opcoes_disponiveis[option]] = tempo_total
    print(f'Tempo calculado para {opcoes_disponiveis[option]}: {tempo_total:.2f} segundos.')
    del opcoes_disponiveis[option]


# Soma do tempo total de cada oção
def total_timer():
    print('Tempo gasto em cada opção:')
    for title, time in test_timer.items():
      if time != 0:  # Verifica se o tempo individual é diferente de zero
        print(f'{title}: {time:.2f} segundos.')
    
    total = sum(test_timer.values())
    print(f'\nTempo total: {total:.2f} segundos.')


def main():
  while True:
    print('Teste KLM - Inteface de Aplicações Informáticas\n')

    # Mostrar opções
    for option, title in opcoes_disponiveis.items():
      if test_timer[title] == 0:
        print(f'{option}. {title}')
      else:
        print(f'{option}. {test_timer[title]:.2f}: segundos.')

    print('7. Calcular Tempo Total')
    print('0. Sair do programa')

    option = user_input()

    if option in opcoes_disponiveis:
      clear_screen()
      calculate_timer(option)
      sleep(1)
      clear_screen()
    elif option == 7:
      clear_screen()
      total_timer()
      break
    elif option == 0:
      clear_screen()
      print('Adeus!')
      break

if __name__ == '__main__':
  main()