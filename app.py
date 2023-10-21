# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Corbin Sy" # write your name
    age = "16" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    fatherN = 'Paul'
    fatherA = '49'
    return render_template('father.html', name = fatherN, age = fatherA)

# define the route to mother webpage
@app.route("/mother")
def mother():
    motherN = 'Sarah'
    motherA = '39'
    return render_template('mother.html', name = motherN, age = motherA)

# define the route to friends webpage
@app.route("/friends")
def friends():
    frN = 'Dacey'
    frA = '16'
    return render_template("friend.html", name = frN, age = frA )

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
