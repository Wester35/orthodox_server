from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the main page"


@app.route('/sign_up', methods=['GET'])
def registration_page():
    return render_template('sign_up.html')


@app.route('/register', methods=['POST'])
def register():
    # Здесь будет ваша логика обработки регистрации
    username = request.form['username']
    password = request.form['password']
    # Здесь будет код для работы с базой данных
    return f"User {username} registered successfully!"


@app.route('/sign_in', methods=['GET'])
def login_page():
    return render_template('sign_in.html')


@app.route('/sign_in', methods=['POST'])
def login():
    # Здесь будет ваша логика аутентификации
    username = request.form['username']
    password = request.form['password']
    return f"User {username} logged in successfully!"

if __name__ == '__main__':
    app.run(debug=True)