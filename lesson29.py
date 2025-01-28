# def func(text:str) -> list:
#     return list(text)
#
# print(func('hello'))


# number = input()
# numbers = ()
# try:
#     print(int(number * 2))
# except ValueError:
#     print('Вводите тольк очисла!')
#
# try:
#     numbers.append(number)
# except AttributeError:
#     print('В кортеж нельзя добавлять данные!')


# m = 34
# spam = 'hello'
#
# try:
#     m + spam
# except TypeError:
#     print('Ошибка в данных')




# try:
#     spammer = (10, 11, 12)
#     spammer.append(13)
# except AttributeError:
#     print('В кортеж нельзя добавлять данные!')


import logging

logging.basicConfig(filename='first.log',
                    filemode='a',
                    format='%(asctime)s || %(name)s || %(levelname)s || %(message)s')

logging.debug('privet')
logging.info('zdarov')
logging.warning('poka')
logging.error('Bugaga')
logging.critical('moskva')
