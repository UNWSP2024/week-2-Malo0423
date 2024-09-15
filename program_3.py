def calculate_total_purchase():
    print("Please enter price of items below.")
    item1 = int(input('Item 1: '))
    item2 = int(input('Item 2: '))
    item3 = int(input('Item 3: '))
    item4 = int(input('Item 4: '))
    item5 = int(input('Item 5: '))
    subtotal = item1 + item2 + item3 + item4 + item5
    tax = subtotal * 0.07
    total = subtotal + tax
    print('Your subtotal is $', format(subtotal, ',.2f'),)
    print('Your tax is $', format(tax, ',.2f'),)
    print('\n\nYour total is', format(total, ',.2f'),)
calculate_total_purchase()