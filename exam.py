from flask import Flask


app = Flask(__name__)

@app.route('/hello')
def hello():
  return '<h1>こんにちは<h1>'

@app.route('/hello/<post_1>/<post_2>')
def show_post(post_1, post_2):
  return '<h1>こんにちは{}さん{}さん<h1>'.format(post_1, post_2)

@app.route('/add/<int:num1>/<int:num2>')
def show_add(num1, num2):
  num = num1 + num2
  return '<h1>{}<h1>'.format(num)

@app.route('/div/<float:num1>/<float:num2>')
def show_num(num1, num2):
  return '<h1>{}<h1>'.format(num1 // num2)



if __name__=='__main__':
  app.run(debug=True)