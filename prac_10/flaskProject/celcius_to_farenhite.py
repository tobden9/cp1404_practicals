from flask import Flask, request, render_template

app = Flask(__name__)

# Define the Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Define the route for temperature conversion
@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"<p>{celsius_float} Celsius is equal to {fahrenheit} Fahrenheit.</p>"
    except ValueError:
        return "<p>Invalid input. Please provide a valid number for Celsius.</p>"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)