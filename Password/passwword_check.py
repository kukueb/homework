import password_contaiment

pass_try = 0

if password_contaiment.password == "0":
    password_contaiment.password = input('Создайте пароль: ')
    f = open('password_contaiment.py', 'w') 
    f.write(f'password = "{password_contaiment.password}"')
    f.close()

else:
    while pass_try != password_contaiment.password:
        pass_try = input('Введите пароль: ')
        if pass_try == '':
            exit()
        elif pass_try != password_contaiment.password:
            print('Пароль неверный! Попробуйте войти ещё раз.')
print("Вы успешно вошли в учётную запись!")
