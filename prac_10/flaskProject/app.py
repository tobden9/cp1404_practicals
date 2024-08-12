from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


# Define the greet route without a parameter
@app.route('/greet')
# Define the greet route with a parameter
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


if __name__ == '__main__':
    app.run()
