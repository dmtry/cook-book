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
@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    return render_template("recipe.html", recipes=mongo.db.recipes.find({"_id": ObjectId(recipe_id)}))

    
#add new recipe page
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', 
        categories=mongo.db.categories.find())

#submit new recipe
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

#edit recipe
@app.route ('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    #the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template("edit_recipe.html", recipe=the_recipe, categories=all_categories)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)