"""
Выполнил студент Ханов Д.С

Задание ИСР 2.3
"""


def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    elif (n == 0):
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

def slise(f, j, i = 0):
  """
  j - до какого элемента -1 (т.к индексация идет с 0)
  i - с какого элемента(по умолчанию 0) 
  f - list с сенерированными числами фиббоначи
  """
  return f[i:j]

fib_list = []
for i in range (0, 23):
  fib_list.append(fibonacci(i))

print(fib_list)

print(slise(fib_list, 12))

print(slise(fib_list, 12, 10))

print(slise(fib_list, 12, 9))

