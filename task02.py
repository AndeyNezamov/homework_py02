# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


from fractions import Fraction

first_fraction = input('Введите первую дробь в формате a/b: ')
second_fraction = input('Введите вторую дробь в формате a/b: ')

first_numerator, first_denominator = map(int, first_fraction.split('/'))
second_numerator, second_denominator = map(int, second_fraction.split('/'))

sum_fraction_numerator = first_numerator * second_denominator + second_numerator * first_denominator
sum_fraction_denominator = first_denominator * second_denominator

count_sum = 2
while count_sum<sum_fraction_denominator:
    if sum_fraction_numerator % count_sum == 0 and sum_fraction_denominator % count_sum == 0:
        sum_fraction_numerator = sum_fraction_numerator / count_sum
        sum_fraction_denominator = sum_fraction_denominator / count_sum
    else:
        count_sum += 1

print(f'Сумма дробей = {int(sum_fraction_numerator)}/{int(sum_fraction_denominator)}')
print(Fraction(first_numerator, first_denominator) + Fraction(second_numerator, second_denominator))

multiplication_numerator = first_numerator * second_numerator
multiplication_denominator = first_denominator * second_denominator

count_mult = 2
while count_mult < multiplication_denominator:
    if multiplication_numerator % count_mult == 0 and multiplication_denominator % count_mult == 0:
        multiplication_numerator = multiplication_numerator / count_mult
        multiplication_denominator = multiplication_denominator / count_mult
    else:
        count_mult += 1

print(f'Произведение дробей = {int(multiplication_numerator)}/{int(multiplication_denominator)}')
print(Fraction(first_numerator, first_denominator) * Fraction(second_numerator, second_denominator))
