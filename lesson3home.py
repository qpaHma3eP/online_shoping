contact_list = ['Дильшод', 'Шухрат', 'Эркин', 'Фарзона']
print(f'Cписок контактов {contact_list}')
contact = input('Введите действие: Добавить, Изменить или Удалить: ')
if contact == 'Добавить':
        new_contact = input('Введите имя: ')
        contact_list.append(new_contact)
        print('Контакт добавлен')
        print(contact_list)
elif contact == 'Изменить':
        change_contact = input('Введите контакт который хотите изменить: ')
        contact_list[0]:[4] = input('Введите новый контакт: ')
        print('Контакт изменен')
        print(contact_list)
elif contact == 'Удалить':
        delete_contact = input('Введите контакт который хотите удалить: ')
        contact_list.remove(delete_contact)
        print('Контакт удален')
        print(contact_list)
else:
        print('Попробуйте заного!')