print('Введите количество вводимых числе от 1 до 10000:')
numberArray = []
NUMBER_LIMIT = 10000
n = int(input('N = '))
if n > NUMBER_LIMIT: 
    print('Неверное количество символов')
else:
     for i in range(n):
          number = int(input(f'Число #{i + 1} = '))
          if abs(number) > NUMBER_LIMIT: 
               print('Превышен допустимы диапазон')
               break
          numberArray.append(number)

print(list(reversed(numberArray)))