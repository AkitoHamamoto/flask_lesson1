for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('{}: Fizz Buzz'.format(i))
  elif i % 3 == 0:
    print('{}: Fizz'.format(i))
  elif i % 5 == 0:
    print('{}: Buzz'.format(i))
  else:
    print(i)
else:
  print('ループ処理実行完了')