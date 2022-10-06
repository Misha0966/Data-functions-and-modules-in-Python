# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
num_fib = int(input('Задайте число k, для составления списка чисел Фибоначчи, в том числе для отрицательных индексов: '))

def list_fib(num_fib): # Задаём функцию, которая составит список чисел Фибоначчи, в том числе для отрицательных индексов.
    fib_list = [1] * (2 * num_fib + 1) # создаём переменную fib_list и присваем ей значения в виде произведения первого индекса списка и переменной num_fib *2 и +1
    fib_list[num_fib] = 0 # переменной fib_list со значениями num_fib присваиваем значение 0
    for i in range(num_fib + 2, len(fib_list)): # пока переменная i находится в промежутке переменной num_fib+2 и длины списка fib_list, то тогда
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2] # списку Фибоначчи со значениями переменной i присваем значениями суммы списка Фибоначчи переменной i-1 и списка Фиббоначи со значениями переменной i-2 
        fib_list[len(fib_list) - i - 1] = fib_list[i] * (-1) ** (i + 1) # формула для списка Фибоначчи, в том числе для отрицательных индексов

    print(fib_list)

list_fib(num_fib)