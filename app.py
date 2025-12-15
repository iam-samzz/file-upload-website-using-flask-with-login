from flask import Flask,redirect,render_template,session,request
import os

from db.insert_file import run_insert_func

from flask_session import Session



app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html",name = session.get("name"))



@app.route("/upload",methods=['POST'])
def upload():
    name = request.form.get("name")
    file = request.files.get("pdf")

    if not name or not file:
        return redirect("/")
    


    filename = file.filename
    input_list = [name,filename]


    file.save(f'uploads/{filename}')



    run_insert_func(input_list)


    return redirect("/")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html");


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)