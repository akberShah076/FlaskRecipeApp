from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '74382d46f8ad421fac4ce0274b3c4d0a'
API_URL = 'https://api.spoonacular.com/recipes/complexSearch'

def fetch_recipes(ingredients):
    params = {
        'apiKey': API_KEY,
        'includeIngredients': ','.join(ingredients),
        'number': 10,  # Number of recipes to fetch
        'addRecipeInformation': True
    }
    response = requests.get(API_URL, params=params)
    return response.json().get('results', [])

@app.route("/", methods=['GET', 'POST'])
def home():
    matching_recipes = []
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        if ingredients:
            ingredients_list = [ingredient.strip() for ingredient in ingredients.split(',')]
            matching_recipes = fetch_recipes(ingredients_list)
    return render_template('home.html', recipes=matching_recipes)

if __name__ == '__main__':
    app.run(debug=True)
