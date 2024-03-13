from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host='sql6.freemysqlhosting.net', user='sql6690843',password='TCgWWYv9da',database='sql6690843')
cursor = conn.cursor()

@app.route('/')
def login():
  if 'user_id' in session:
    return redirect('/home')
  return render_template('login.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
  email = request.form.get('email')
  password = request.form.get('password')

  cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))

  users = cursor.fetchall()
  
  if len(users)>0:
    session['user_id'] = users[0][-1]
    print(session['user_id'])
    return redirect('/home')
  return redirect('/')

@app.route('/register')
def register():
  if 'user_id' in session:
    return redirect('/home')
  return render_template('register.html')

@app.route('/add_user',methods=['POST'])
def add_user():
  email = request.form.get('email')
  password = request.form.get('password')
  last_name = request.form.get('last_name')
  first_name = request.form.get('first_name')

  cursor.execute("""INSERT INTO `users` (`first_name`, `last_name`, `email`, `password`, `id`) VALUES ('{}', '{}', '{}', '{}', NULL)""".format(first_name, last_name,email, password))
  conn.commit()

  cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))

  users = cursor.fetchall()
  
  if len(users)>0:
    session['user_id'] = users[0][-1]
    print(session['user_id'])
    return redirect('/home')
  return redirect('/register')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/home')
def home():
  if 'user_id' in session:
    return render_template('home.html')
  return redirect('/')

@app.route('/logout')
def logout():
  session.pop('user_id')
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)