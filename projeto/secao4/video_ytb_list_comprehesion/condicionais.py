numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [number for number in numbers if number > 5]
odd = [number for number in numbers if number % 2 != 0]
pair = [number for number in numbers if number % 2 == 0]
# Acima temos o modelo de filter
another_type_if = [
    number
    if number != 6 else 600
    for number in pair
]

print(numbers)
print(new_numbers)
print(odd)
print(pair)
print(another_type_if)
