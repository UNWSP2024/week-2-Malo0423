def temp_conversion(celsius):

    fahrenheit = 0.0
    fahrenheit += celsius*9.0/5.0 + 32

    return fahrenheit


if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0

    celsius = float(input('Enter a temperature in celsius: '))
    fahrenheit = temp_conversion(celsius)

    print('\nThat is equal to', format(fahrenheit, '.2f'), 'degrees Fahrenheit')
