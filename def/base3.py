# グローバル変数

def printAnimal():
  global animal
  animal = 'Cat'
  print('関数内animal = {}, id = {}'.format(animal, id(animal)))

try:
  printAnimal()
  print('関数外animal = {}, id = {}'.format(animal, id(animal)))
except Exception as e:
  print('エラーが発生しました', e, type(e))