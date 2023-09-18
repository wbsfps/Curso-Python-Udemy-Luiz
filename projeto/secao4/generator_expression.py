import sys

# Generator expression- função que sabem pausar, Iterables e Iterators em Python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

list_ = [number for number in range(10000)]
generator = (number for number in range(10000))

print(sys.getsizeof(list_))  # valor em bytes
print(sys.getsizeof(generator))  # valor em bytes

print(next(generator))

for number in generator:
    print(number)
