# デフォルト値　可変長引数 複数返り値

def sample(arg1, *arg2):
  print('arg1 = {}, arg2 = {}'.format(arg1, arg2))

sample(1,2,3,4,5,6)

def sample2(arg1, **arg2):
  print('arg1 = {}, arg2 = {}'.format(arg1, arg2))

sample2(3, name='taro', age=20)


def sample3():
  return 1,2,3

a,b,c = sample3()
print(a,b,c)