from flask import Flask, render_template,request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://hmlzedxmyiixoc:881761f4937ebeaaba755f03aec7f8f4449d2f0ad0d35f8ac78019e371ae9499@ec2-18-210-214-86.compute-1.amazonaws.com:5432/dekf5v3rogk5p2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# setting up the secret key for the application
app.config['SECRET_KEY'] = 'f9a1520561f1faf67f36a3a620a45e80'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/result', methods=['GET','POST'])
def result():
    full_name = request.form.get("FUll_name")
    user_name = request.form.get("user_name")
    email = request.form.get("email_name")
    password = request.form.get("password_name")
    user_obj = User(FullName = full_name, username = user_name, email = email, password = password)
    db.session.add(user_obj)
    db.session.commit()
    return render_template('result.html', Username=user_name)

@app.route('/admin')
def admin():
    data = User.query.all()
    print(data[0].username)
    return render_template('admin.html', data = data)

@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get("user_name")
        password = request.form.get("password_name")
        print(user_name)
        print(password)
        user_obj = User.query.filter_by(username = user_name).first()
        if password == user_obj.password and  user_name == user_obj.username:
            session["USERNAME"] = user_name
            return redirect(url_for("profile"))
    return render_template('login.html')

@app.route('/profile', methods=['post'])
def profile():
    if session.get("USERNAME") is not None:
        return render_template('profile.html' , user_name = session.get("USERNAME"))
    else:
        return redirect(url_for("login"))    


if __name__ == "__main__":
    app.run(debug=True)



