under_liter = 0.10
over_liter = 0.25
while True:
    bottle_1 = int(input('Введите количество бутылок до 1 л: '))
    bottle_2 = int(input('Введите количество бутылок больше 1 л: '))
    overall = (bottle_1 * under_liter) + (bottle_2 * over_liter)
    print(f'Вы получаете ${round(overall, 2)}')