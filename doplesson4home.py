under_liter = 0.10
over_liter = 0.25
while True:
    bottle_1 = int(input('Введите количество бутылок до 1 л: '))
    bottle_2 = int(input('Введите количество бутылок больше 1 л: '))
    overall = (bottle_1 * under_liter) + (bottle_2 * over_liter)
    print(f'Вы получаете ${round(overall, 2)}')



# nds = 0.12
# tips = 0.18
# while True:
#     order = int(input('Введите сумму заказа: '))
#     tip = order * tips
#     tax = order * nds
#     total = order + tip + tax
#     print(f'Налог: ${round(tax, 2)}\n '
#           f'Чаевые: ${round(tip, 2)}\n '
#           f'Итог: ${round(total, 2)}')



# while True:
#     nums = int(input('Введите число-границу: '))
#     sum = (nums) * (nums + 1) / 2
#     print(sum)



# souv = 75
# trinket = 112
# while True:
#     souv_count = int(input('Введите количество сувениров: '))
#     trinket_count = int(input('Введите количество безделушек: '))
#     print(f'{(souv_count * souv) + (trinket_count * trinket)} грамм')