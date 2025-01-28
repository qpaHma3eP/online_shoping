souv = 75
trinket = 112
while True:
    souv_count = int(input('Введите количество сувениров: '))
    trinket_count = int(input('Введите количество безделушек: '))
    print(f'{(souv_count * souv) + (trinket_count * trinket)} грамм')