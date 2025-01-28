number1 = int(input('Введите первое число: '))
mat_oper = input('Выберите действие (+ - * /): ')
number2 = int(input('Введите второе число: '))
if mat_oper == '+':
    print(number1+number2)
elif mat_oper == '-':
    print(number1-number2)
elif mat_oper == '*':
    print(number1*number2)
elif mat_oper == '/':
    print(number1/number2)
else:
    print('Такое действие отсутстует')
