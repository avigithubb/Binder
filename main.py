import sqlalchemy.exc
from PIL.Image import Image
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask import redirect
from flask import url_for
from forms import LoginForm
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_gravatar import Gravatar
import sqlite3
import io
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]

db = SQLAlchemy()
db.init_app(app)
conn = sqlite3.connect("C://Users/Abhishek/PycharmProjects/Udemy tuts/Binder/instance/users.db", check_same_thread=False)
cursor = conn.cursor()

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    occupation = db.Column(db.String(100))
    residence = db.Column(db.String(250))
    qualification = db.Column(db.String(100))
    zodiac = db.Column(db.String(100))
    height = db.Column(db.Integer)
    fav_food = db.Column(db.String(100))
    language = db.Column(db.String(100))
    passion = db.Column(db.String(100))
    status = db.Column(db.String(100))
    image = db.Column(db.String(100))


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route('/create_account', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        image = request.files['image'].read()
        image_blob = io.BytesIO(image)
        query = 'INSERT INTO User (image) VALUES (?)'

        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
            name=request.form.get("username"),
            occupation=request.form.get("occupation"),
            residence=request.form.get("address"),
            qualification=request.form.get("qualification"),
            zodiac=request.form.get("zodiac"),
            height=request.form.get("height"),
            fav_food=request.form.get("food"),
            language=request.form.get("lang"),
            passion=request.form.get("passion"),
            status=request.form.get("social"),
            image=image_blob.read()
        )
        try:

            db.session.add(new_user)
            db.session.commit()
            conn.commit()
            # cursor.close()
            # conn.close()
        except sqlalchemy.exc.IntegrityError:
            flash("You've already signed up with that email, Log in instead!")
            return redirect(url_for("login"))

        return redirect(url_for("login", user_id=new_user.id))
    else:
        return render_template("create_account.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user_email = request.form.get("email")
        if user_email not in db.session.execute(db.select(User.email)).scalars().all():
            flash("The email does not exist,please try again!")
            return redirect(url_for("login"))
        user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        if not check_password_hash(user.password, password=request.form.get("password")):
            flash("The password is incorrect,please try again!")
            return redirect(url_for("login"))
        if check_password_hash(user.password, password=request.form.get("password")):
            query = 'SELECT image FROM User WHERE id = ?;'
            cursor.execute(query, (user.id,))
            image_blob = cursor.fetchone()[0]
            image = io.BytesIO(image_blob)
            image = Image.load(user.image)
            # print(image)
            login_user(user, force=True)
            return redirect(url_for('bind', user_id=user.id, logged_in=True, user_email=user.email, gravatar_email=gravatar(email=user.email), user=user))
    return render_template("login.html", form=form)


@app.route('/download', methods=["GET", "POST"])
def download():
    return render_template("download.html")


@app.route('/learn', methods=["GET", "POST"])
def learn():
    return render_template("learn.html")


@app.route('/safety', methods=["GET", "POST"])
def safety():
    return render_template("safety.html")


@app.route('/support', methods=["GET", "POST"])
def support():
    return render_template("support.html")


@app.route('/binder', methods=["GET", "POST"])
def bind():
    return render_template("bind.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
