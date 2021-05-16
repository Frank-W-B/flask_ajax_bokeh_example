from flask import Flask
from bokeh.models.sources import AjaxDataSource

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World."

if __name__ == '__main__':
    app.run(debug=True)
