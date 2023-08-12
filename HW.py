from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/clothes/')
def clothes():
    return render_template('Clothes.html')

@app.route('/jacket/')
def jacket():
    return render_template('Jackets.html')

@app.route('/shoes/')
def shoes():
    return render_template('Foodwear.html')



if __name__ == '__main__':
    app.run()