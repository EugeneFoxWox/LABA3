def inputs():
   while True:
       x = int(input('Введите натур. число '))
       if x > 0:
           break
       print('Неверное число')
   return x
  

def x2(x):
  x/= 2
  return collatz(x)


def x3_1(x):
  x = x*3 + 1
  return collatz(x)
  

def collatz(x):
  result = [x]
    if x == 1:
       pass
    elif x%2 == 0:
         result.extend(x2(x))
    else:
        result.extend(x3_1(x))
    return result
  

if __name__ == '__main__':
  N = inputs()
  print(collatz(N))

   
