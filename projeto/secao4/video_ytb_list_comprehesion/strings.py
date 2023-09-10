string = 'William Batista'
number_letters = 1
new_string = '.'.join([
    string[index:index + number_letters]
    for index in range(0, len(string), number_letters)
])

print(new_string)
