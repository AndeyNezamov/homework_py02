# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

alphabet = '0123456789abcdef'
number = int(input('Введите число: '))
new_number = ''
print(hex(number)[2:])
while number > 0:
    new_number = alphabet[number % 16] + new_number
    number //= 16
print(new_number)