from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def home_page():
    fav_food = ['cheeseburger', 'puree batata','apples']
    return render_template('index.html',
                           fav_food = fav_food)

if __name__ == '__main__':
   app.run(debug = True)
