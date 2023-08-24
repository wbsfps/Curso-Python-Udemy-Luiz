def negative_or_positive(number):
    if number > 0:
        return 'P'
    return 'N'


positive = negative_or_positive(3)
negative = negative_or_positive(-1)

print(negative)
print(positive)
