import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# db connect
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:DOOMiddqd666@myfirstcluster-labih.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

#get recipes page
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
#get single recipe page
@app.route('/')
@app.route('/get_recipe')
def get_recipe():
    return render_template("recipe.html", recipes=mongo.db.recipes.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)