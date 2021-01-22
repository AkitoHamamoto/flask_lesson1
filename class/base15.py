# with base15.py

class WithTest:

  def __init__(self, msg):
    print('init called')
    self.msg = msg

  def __enter__(self):
    print('enter called')
    print(self.msg)

  def __exit__(self, exc_type, exc_val, traceback): #エラーハンドリングのために引数を3つ用意する名前はなんでもいいが慣習的にこの三つが用いられる
    print('exit called')

with WithTest('Hello') as t:
  print('With の中')

class WithTest:

  def __init__(self, file_name):
    print('init called')
    self.__file_name = file_name

  def __enter__(self):
    print('enter called')
    self.__file = open(self.__file_name, mode='a', encoding='utf-8')
    return self

  def write(self, msg):
    self.__file.write(msg)

  def __exit__(self, exc_type, exc_val, traceback):
    print('exit called')
    self.__file.close()

with WithTest('resources/output.txt') as t:
  print('With の中')
  t.write('ああああああ')
