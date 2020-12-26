# Import required packages
import os
from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Displays the home page accessible at the addresss '/'
@app.route("/")
def home():
    # Render the html page
    return render_template(
        "home.html",
    )


# Run the application
if __name__ == "__main__":
    app.run(
        debug=True, port=int(os.getenv("PORT", 8080)), host=os.getenv("IP", "0.0.0.0")
    )
