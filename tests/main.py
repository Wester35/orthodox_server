from quart import Quart, render_template, request

app = Quart(__name__)


@app.route('/')
@app.route('/home')
async def index():
    return "Welcome to the main page"


@app.route('/sign_up', methods=['GET'])
async def registration_page():
    return await render_template('sign_up.html')


@app.route('/sign_up', methods=['POST'])
async def register():
    data = await request.form
    username = data['username']
    password = data['password']
    print(f"R username: {username}, password: {password}")
    return f"User {username} registered successfully!"


@app.route('/sign_in', methods=['GET'])
async def login_page():
    return await render_template('sign_in.html')


@app.route('/sign_in', methods=['POST'])
async def login():
    data = await request.form
    username = data['username']
    password = data['password']
    print(f"L username: {username}, password: {password}")
    return f"User {username} logged in successfully!"

if __name__ == '__main__':
    app.run(debug=True)