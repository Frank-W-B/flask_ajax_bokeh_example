from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World."

if __name__ == '__main__':
    app.run(debug=True)
