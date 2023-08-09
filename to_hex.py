number = int(input("введите число: "))
print(hex(number))

hex_digits = '0123456789abcdef'
if number == 0:
    print('0x0')
else:
    hex_result = ''
    while number > 0:
        hex_result = hex_digits[number % 16] + hex_result
        number //= 16
    print(f'0x{hex_result}')

