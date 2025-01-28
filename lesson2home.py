(print('Добропожаловать и игру камень ножницы бумага'))
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
deystviye1 = int(input(f'Выберите действие {1, 2, 3} для первого игрока: '))
deystviye2 = int(input(f'Выберите действие {1, 2, 3} для второго игрока: '))
deystviye1 == 1, 2, 3
deystviye2 == 1, 2, 3
if deystviye1 == 1 and deystviye2 == 1:
        print('Ничья')
elif deystviye1 == 2 and deystviye2 == 1:
        print('Победил 2й игрок')
elif deystviye1 == 3 and deystviye2 == 1:
        print('Победил 1й игрок')
elif deystviye1 == 1 and deystviye2 == 2:
        print('Победил 1й игрок')
elif deystviye1 == 1 and deystviye2 == 3:
        print('Победил 2й игрок')
elif deystviye1 == 2 and deystviye2 == 2:
        print('Ничья')
elif deystviye1 == 2 and deystviye2 == 3:
        print('Победил 1й игрок')
elif deystviye1 == 3 and deystviye2 == 3:
        print('Ничья')
else:
        print('Выберите действие заного')



