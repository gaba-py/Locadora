import os

carros = [
    ('Toyota Corolla', 120),
    ('Honda Civic', 140),
    ('Ford Mustang', 100),
    ('Chevrolet Onix', 130),
    ('Volkswagen Golf', 80),
    ('Hyundai Tucson', 90),
    ('Jeep Compass', 110)
    ]

alugados = []

def show_car_list(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print(f'[{i}] {car[0]} - R$ {car[1]} /dia.')

print('======')
print('Bem-vindo a locadora de carros!')
print('======\n')

while True:
    print('Oque deseja fazer ?')
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input('Insira uma opção:   '))

    if op == 0:
        show_car_list(carros)

    elif op == 1:
        show_car_list(carros)
        print('===========')
        print('Digite o codigo do carro:  ')
        cod_car = int(input())
        nome_car = carros[cod_car][0]
        print('Digite o número de dias:   ')
        dias = int(input())
        print(f'\nVocê escolheu {nome_car} por {dias} dias.')
        print(f'O aluguel totalizaria R$ {dias * carros[cod_car][1]}. Deseja alugar ?')
        print('\n0 - SIM | 1 - NÃO')
        dec = int(input(''))
        if dec == 0:
            print(f'Parabéns você alugou o carro {nome_car} por {dias} dias.')
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
             print('Não há carros para devolver.')
             os.system('cls')
        else:
            print('Segue a lista de carros alugados. Qual você quer devolver ?')
            show_car_list(alugados)
            print('\nDigite o código do carro que deseja devolver: ')
            cod_car = int(input())
            if dec == 0:
                print(f'Obrigado por devolver o carro {cod_car}.')
                carros.append(alugados.pop(cod_car))
    print('\n==========')
    print('0 para CONTINUAR | 1 para SAIR')
    if float(input()) == 1:
        break