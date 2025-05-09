from flask import Flask, render_template

app = Flask(__name__)
tree_names = ["Tree Name", "Garden Croton", "Bougainvillea"]
tree_details = [
    "Colorful ornamental shrub with variegated foliage in vibrant green, yellow, red, and orange hues.",
    "Colorful ornamental shrub with variegated foliage in vibrant green, yellow, red, and orange hues.",
    "Vibrant flowering vine featuring papery bracts in magenta, purple, and orange hues."
]
tree_images = [
    "../static/images/VisualMatches.jpg",
    "../static/images/GardenCroton.jpg",
    "../static/images/Bougainvillea.jpg"
]
@app.route("/")
def home():
    return render_template("index.html",tName=tree_names,tDetail=tree_details,tImage=tree_images)


@app.route("/Tinfo.html")
def tinfo():
    return render_template("Tinfo.html")








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



@app.route("/trees/info/<nam>")

treeinfo = {
    "" 
}

def infos(nam):
    return render_template("Tinfo.html")




app.run(debug=True)
