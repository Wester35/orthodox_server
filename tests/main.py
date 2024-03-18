from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@5.228.52.190/from_flask'
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username


@app.route('/')
@app.route('/home')
def index():
    return "Welcome to the main page"


@app.route('/sign_up', methods=['GET'])
def registration_page():
    return render_template('sign_up.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    return f"User {username} registered successfully!"


@app.route('/sign_in', methods=['GET'])
def login_page():
    return render_template('sign_in.html')


@app.route('/sign_in', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    return f"User {username} logged in successfully!"


# @app.route('/api/endpoint/')
# def process_request():
#     data = request.json
#     if 'usrName' in data and 'usrPasswd' in data:
#         return jsonify(data)
#     else:
#         # Если какое-то поле отсутствует, возвращаем ошибку
#         return jsonify({'error': 'Missing fields in request'}), 400
@app.route('/api/endpoint/', methods=['POST'])
def process_data():
    # Получаем данные из тела POST-запроса
    user_name = request.form.get('usrName')
    password = request.form.get('usrPasswd')

    # Обработка полученных данных
    # Например, можно отправить их обратно в виде JSON-ответа
    return jsonify({
        'status': 'success',
        'userName': user_name,
        'password': password
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7865, debug=True)