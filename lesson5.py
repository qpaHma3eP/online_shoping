# nums = [i for i in range(100)]
# print(nums)


# my_list = [1, 2, 4.5]
# my = [i + 2 for i in my_list]
# print(my)


# my = ['2', '33', 'Jordan', 'Paver']
# my2 = [i + '2' for i in my]
# print(my2[1:3])


# names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
# answer = [i[0] for i in names]
# print(answer)


# nums1 = [i for i in range(1, 21)]
# nums2 = [i for i in nums1 if i % 2 != 0]
# print(nums2)


# usernames = []
# while True:
#     newnames = input('Введите юзернейм: ')
#     if newnames in usernames:
#         print('Такой юзер существует')
#
#     else:
#         usernames.append(newnames)
#         print('Юзернейм добавлен')
#         print(usernames)


# nums = [1, 2, 3, 4, 5]
# my_list = [i for i in range(1, 5) if i in nums]
# print(my_list)


# nums1 = [i for i in range(1, 21)]
# nums2 = [i for i in nums1 if i % 2 == 0]
# print(nums2)


number = int(input('Введите число, я определю на четность и нечетность: '))
if (number % 2 == 0):
    print('Это четное число')
elif (number % 2 != 0):
    print('Это нечетное число')
else:
    print('Ошибка при вводе')




