from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.user import Users


@app.route('/')
def index():
    return render_template("create.html")


@app.route('/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    user = Users.get_user(data)
    return render_template("show(one).html",user=user)


@app.route('/edit/<int:id>')
def update(id):
    data = {
        "id":id
    }
    user = Users.get_user(data)
    return render_template("/user_edit.html",user=user)


@app.route('/edituser/<int:id>',methods=['POST'])
def edituser(id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id":id
    }
    Users.edituser(data)
    return redirect("/users")


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Users.delete(data)
    return redirect("/users")

@app.route('/users/new',methods=['POST'])
def guess():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    Users.save(data)
    return redirect('/users')

@app.route('/users')
def users():
    users = Users.get_all()
    return render_template('read(all).html', users = users)

@app.route("/create")
def create():
    return redirect("/")