from flask import Flask, render_template

# Initialize the Flask application
# It expects HTML files to be inside a folder named 'templates'
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    """Route to serve the portfolio website."""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask server on port 5000
    # Debug=True allows the server to auto-reload when you make code changes
    print("Starting Portfolio Server at http://127.0.0.1:5000/")
    app.run(debug=True, port=5000)