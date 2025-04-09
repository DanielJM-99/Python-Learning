def apply_to_each(func, iterable):
    return [func(x) for x in iterable]

def square(x):
    return x * x

def double(numero):
    return numero * 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_to_each(square, numbers)
numeros_por_dos = apply_to_each(double, numbers)
print(squared_numbers) # Output: [1, 4, 9, 16, 25]
print(numeros_por_dos)
