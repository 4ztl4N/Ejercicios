#Ejemplo de iterador

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

text = "Hola mundo"
iter_text = iter(text)
for char in iter_text:
    print(char)

limit = 10
odd_itter = iter(range(1,limit+1,2))
for num in odd_itter:
    print(num)

def my_generator():
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)

#Fibonacci generador
def fibonacci(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b
for num in fibonacci(10):
    print(num)


#generador impar
def num_impar(limit):
    a = 1
    while a< limit+1:
        yield a
        a= a+2
for impar in num_impar(30):
    print(impar)
    

#generador par
def num_par(limit):
    a = 0
    while a< limit+1:
        yield a
        a= a+2
for par in num_par(30):
    print(par)

