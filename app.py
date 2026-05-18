import os

from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv

from models import db, User

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        username=request.form.get("username")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).filter_by(username=username)).scalar()

        if user:
            if user.password == password:
                session["username"] = user.username
                session["email"] = user.email

                if user.username == "admin":
                    return redirect(url_for("user_list"))
                else:
                    return redirect(url_for("user_profile"))
            else:
                return "密碼錯誤！"
        else:
            return "查無此使用者！"
    return render_template("index.html")

@app.route("/userlist")
def user_list():
    if "username" not in session or session["username"] != "admin": 
        return redirect(url_for("user_login"))
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
        return redirect(url_for("user_login"))
    return render_template("register.html")

@app.route("/profile")
def user_profile():
    if "username" not in session:
        return redirect(url_for("user_login"))
    current_user = {
        "username": session["username"],
        "email": session["email"]
    }
    return render_template("profile.html", user=current_user)

@app.route("/logout")
def user_logout():
    session.clear() 
    return redirect(url_for("user_login"))

app.run()