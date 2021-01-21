#　関数

def print_hello(name):
  print('こんにちは{}さん'.format(name))

print_hello('apkpkvpv')

def num_max(a, b):
  print('a = {}, b = {}'.format(a, b))
  if a > b:
    return a
  else:
    return b
print(num_max(30, 20))