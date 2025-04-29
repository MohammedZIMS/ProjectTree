from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
name = ["Alif lombu", "Farzana", "Alif ashraf", "Mehedi", "Rafi", "Sokina"]
batch = ["27th", "27th", "26th", "26th", "24th", "20000th"]
age = [20, 23, 22, 22, 25, 20]



@app.route("/info")
def info():
      return render_template("test.html", name=name, batch=batch, age=age, ln=len(name))



@app.route("/info/<int:aage>")
def search(aage):
    name = ["Alif lombu", "Farzana", "Alif ashraf", "Mehedi", "Rafi", "Sokina"]
    batch = ["27th", "27th", "26th", "26th", "24th", "20000th"]
    age = [20, 23, 22, 22, 25, 20]
    
    result = None
    for i in range(len(age)):
        if age[i] == aage:
            result = {"name": name[i], "batch": batch[i], "age": age[i]}
            break

    return render_template("test.html", name=name, batch=batch, age=age, ln=len(name), aage=aage, result=result)


app.run(debug=True)
