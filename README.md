# FlowerShopWeb
This is a where we will be making the website for the Flower Website


, you can follow these steps:

1. Place your HTML file in the `templates` folder. For example, if your file is named `example.html`, it should be located at `templates/example.html`.

2. Open the `app.py` file and add a route to render your HTML file. Here's an example:

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/example')
    def example():
         return render_template('example.html')

    if __name__ ==