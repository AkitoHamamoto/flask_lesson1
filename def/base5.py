# ジェネレーター関数

def generetor(max):
  print('ジェネレーター作成')
  for n in range(max):
    try:
      x = yield n
      print('x = {}'.format(x))
      print('yield実行')
    except ValueError as e:
      print('throwを実行しました')
    


gen = generetor(10)
next(gen)
gen.send(100)
# gen.throw(ValueError('Invalid value'))
gen.close()
next(gen)

# for x in gen:
#   print('x = {}'.format(x))