from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import requests
import pyrebase

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  


firebaseConfig = {
  "apiKey": "AIzaSyCX1qfif-u3ekcltDkni2fPNpn2iPggI7g",
  "authDomain": "u-chords.firebaseapp.com",
  "databaseURL": "https://u-chords-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "u-chords",
  "storageBucket": "u-chords.appspot.com",
  "messagingSenderId": "540688013270",
  "appId": "1:540688013270:web:4a85369a8b698a2d4d3677",
  "measurementId": "G-00JXG8V2MC"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

@app.route('/home', methods=['GET', 'POST'])
def home():
   return render_template("home.html")
   

@app.route('/', methods=['GET', 'POST'])
def main():
   if request.method == 'GET':
      return render_template("main.html")
   else:
      email = request.form['email']
      password = request.form['password']
      try:
         login_session['user'] = auth.create_user_with_email_and_password(email, password)
         print(login_session["user"])
         user_id = login_session['user']['localId']
         return render_template("home.html" , error=error)
      except:
         error = "oppsi, try again"
         print(error)
         return render_template("main.html" , error=error)
   

@app.route('/signin', methods=['GET', 'POST'])
def signin():
      if request.method == 'GET':
         return render_template("signin.html")

      else:
         email = request.form['email']
         password = request.form['password']
         try:
            login_session['user'] = auth.log_in_with_email_and_password(email, password)
            return render_template("home.html" , error=error)
         except:
            error = "oppsi, try again"
            print(error)
            return render_template("signin.html" , error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
      if request.method == 'GET':
         return render_template("signup.html")

      else:
         email = request.form['email']
         password = request.form['password']
         try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('home'))
         except Exception as e:
            error = "oppsi, try again"
            print(e)
            return render_template("signup.html" , error=error)


@app.route('/signout', methods=['GET', 'POST'])
def signout():
   login_session['user'] = None
   return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(debug=True)






  