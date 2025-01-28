# all_products = {'Весь склад': {}}
# backet = {}
#
# while True:
#     admin = input('Что сделать? ')
#     if admin.title() == 'Добавить':
#         product_name = input('Введите название продукта: ')
#         product_count = int(input('Введите кол-во продукта: '))
#         all_products['Весь склад'][product_name] = product_count
#     elif admin.title() == 'Продукты':
#         print(all_products)
#     elif admin.title() == 'Купить':
#         product_to_by = input('Введите название продукта: ')
#         if product_to_by in all_products['Весь склад']:
#             product_amout = int(input('Сколько хотите купить? '))
#             if 0 < product_amout <= all_products['Весь склад'][product_to_by]:
#                 backet[product_to_by] = product_amout
#                 all_products['Весь склад'][product_to_by] -= product_amout
#                 print('Продукт успешно перемещен в корзину')
#                 print(backet)
#     elif admin.title() == 'Удалить':
#         product_to_del = input('Введите название продукта: ')
#         backet.pop(product_to_del)
#         print('Продукт успешно удален из корзины')
#         print(backet)
#
#     else:
#         print('Неизвестная операция!')