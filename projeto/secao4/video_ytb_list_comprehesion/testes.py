names = ['Luiz', 'Otavio', 'Antonio ', 'William']

new_names = [
    f'{name[:-1].lower()}{name[-1].upper()}'
    for name in names
    if name.startswith('W')
]
print(new_names)
