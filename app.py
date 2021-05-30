from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/upload-recipe')
def upload_recipe():
    return render_template('upload_recipe.html')

@app.route('/all_recipes')
def all_recipes():
    return render_template('all_recipes.html')

@app.route('/remove_recipe')
def remove_recipe():
    return render_template('remove_recipe.html')

@app.route('/change_recipe')
def change_recipe():
    return render_template('change_recipe.html')


if __name__ == "__main__":
    app.run(debug=True)