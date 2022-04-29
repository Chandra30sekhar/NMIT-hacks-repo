from flask import Flask, render_template, sessions, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from secure import ret_sha1
app = Flask(__name__)


#app conifguration
UPLOAD_FOLDER = './static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

#create a new user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.VARCHAR(100), nullable=False)
    user_password = db.Column(db.VARCHAR(300), nullable=False)
db.create_all()

#homepage
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = ret_sha1(request.form.get('password'))
        name = request.form.get('username')
        new_user = User(user_name=name, user_email=email, user_password=password)
        db.session.add(new_user)
        db.session.commit()
        # flash('Successfully created a new account.')
        return render_template("home.html", n=name)
    return render_template('sample_login.html')



if __name__ == '__main__':
    app.run(debug=True)