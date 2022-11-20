# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyException(Exception):
    def __init__(self, text):
        self.txt = text


def digits_control(string, my_list):
    try:
        if not string.lstrip('-').replace('.', '', 1).isdigit():
            raise MyException("Вы ввели не число")
    except MyException as err:
        print(err)
    else:
        my_list.append(float(string))


digits_list = []
user_str = input('Введите число для заполнения списка или «stop» для выхода: ')
while user_str != 'stop':
    digits_control(user_str, digits_list)
    print(f'Список введенных чисел: \n{digits_list}')
    user_str = input('Введите число для заполнения списка или «stop» для выхода: ')
