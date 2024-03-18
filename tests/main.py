from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


app = Flask(__name__)

load_dotenv()

database_url = os.getenv("DB_URL")


app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class User(db.Model):
    __tablename__ = 'usrs'  # Указываем имя таблицы

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.Integer)
    last_name = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    surname = db.Column(db.String(30), unique=True)
    license = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


@app.route('/')
@app.route('/home')
def index():
    return "Welcome to the main page"


@app.route('/sign_up', methods=['GET'])
def registration_page():
    return render_template('sign_up.html')


@app.route('/register', methods=['POST'])
def register():
    surname = request.form['username']
    password = request.form['password']
    new_user = User(email=surname, password=password, phone=43223,
                    last_name=surname, first_name=surname,
                    surname=surname, license=1)

    db.session.add(new_user)
    db.session.commit()
    return f"User {surname} registered successfully!"


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
# @app.route('/api/endpoint/', methods=['POST'])
# def process_data():
#     # Получаем данные из тела POST-запроса
#     user_name = request.form.get('usrName')
#     password = request.form.get('usrPasswd')
#
#     # Обработка полученных данных
#     # Например, можно отправить их обратно в виде JSON-ответа
#     return jsonify({
#         'status': 'success',
#         'userName': user_name,
#         'password': password
#     })

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=7865, debug=True)


