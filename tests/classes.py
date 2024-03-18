class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = dv.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.Integer)
    last_name = db.Column(db.String(30), unique=True, nullable=False)
    first_name = db.Column(db.String(30), unique=True, nullable=False)
    surname = db.Column(db.String(30), unique=True)
    lincense = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'