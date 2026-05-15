import os

from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

from models import db, User

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
db.init_app(app)

@app.route("/userlist")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars().all()
    return render_template("list.html", users=users)

@app.route("/register", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form.get("username"),
            password = request.form.get("password"),
            email=request.form.get("email"),
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_list"))
    return render_template("register.html")

app.run()