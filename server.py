from flask import Flask, render_template, request, redirect
from users import Users
app = Flask(__name__)
app.secret_key="shhh"


@app.route('/')
def index():
    return render_template("create.html")

@app.route('/users/new',methods=['POST'])
def guess():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
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


if __name__ == "__main__":
    app.run(debug=True)