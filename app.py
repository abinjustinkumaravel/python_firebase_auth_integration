from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Firebase configuration
firebaseConfig = {
#  Add your apikey here;
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session['user'] = user
        return redirect(url_for('dashboard'))
    except:
        return 'Login Failed'

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return 'Welcome to the Dashboard'
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
