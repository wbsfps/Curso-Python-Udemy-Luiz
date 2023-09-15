def show_biggest_number():
    list_numbers = []
    for _ in range(1, 6):
        numbers = input('Enter a number: ')
        numbers_int = int(numbers)
        list_numbers.append(numbers_int)

    biggest_number = min(list_numbers)

    return biggest_number


show_number = show_biggest_number()

print(show_number)
