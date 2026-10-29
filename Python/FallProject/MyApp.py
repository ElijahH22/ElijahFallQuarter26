
from flask import Flask

#Create a new Flask app name "app"
app = Flask(__name__)

# Create a home page for our flask app (website)
@app.route('/')
def Index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)
    