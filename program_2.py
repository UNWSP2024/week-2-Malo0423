def average_age(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

numbers = []
for i in range(5):
    num = int(input('Enter a number: '))
    numbers.append(num)

result = average_age(numbers)
print('The average of the numbers is', result)