# Создайте программу для игры в ""Крестики-нолики"".


def check_for_win(a,symbol):
    game_ended = False
    for i in a:    
        if i == [symbol, symbol, symbol]:
            game_ended = True
    for i in range(3):
        if list(map(lambda line: line[i],a[:])) == [symbol, symbol, symbol]:
            game_ended = True
    if a[0][0] == symbol and a[1][1] == symbol and a[2][2] == symbol:
        game_ended = True
    if a[0][2] == symbol and a[1][1] == symbol and a[2][0] == symbol:
        game_ended = True
    return game_ended

def redraw(a):
    for i in a:
        print(i)
    print()


a = [
[" 1 ", " 2 ", " 3 "],
[" 4 ", " 5 ", " 6 "],
[" 7 ", " 8 ", " 9 "]
]

symbols = {1: ' x ', 2: ' o '}

id_player = 1
game_ended = False
while not game_ended:
    redraw(a)

    if check_for_win(a, symbols[1]):
        print('Игрок 1 победил!')
        break
    if check_for_win(a, symbols[2]):
        print('Игрок 2 победил!')
        break

    print(f'Ходит игрок {id_player} знак - {symbols[id_player]}')

    turn_ended = False
    while not turn_ended:
        N = int(input('Введите число 1...9: '))
        
        for i,line in enumerate(a):
            for j,elem in enumerate(line):
                # print(j,elem)
                if f" {N} "== elem:
                    a[i][j] = symbols[id_player]
                    turn_ended = True
        if turn_ended == False:
            print('Выберите другую ячейку!')
            redraw(a)

    if id_player == 1:
        id_player = 2
    else:
        id_player = 1