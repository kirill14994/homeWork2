from math import gcd

frac1 = input("введите дробь 1: ")
frac2 = input("введите дробь 2: ")

numerator_1, denominator_1 = map(int, frac1.split('/'))
numerator_2, denominator_2 = map(int, frac2.split('/'))

sum_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
sum_denominator = denominator_1 * denominator_2

prod_numerator = numerator_1 * numerator_2
prod_denominator = denominator_1 * denominator_2

sum_gcd = gcd(sum_numerator, sum_denominator)
prod_gcd = gcd(prod_numerator, prod_denominator)

print(f"Сумма дробей: {sum_numerator // sum_gcd}/{sum_denominator // sum_gcd}, "
      f"Произведение дробей: {prod_numerator // prod_gcd}/{prod_denominator // prod_gcd}")