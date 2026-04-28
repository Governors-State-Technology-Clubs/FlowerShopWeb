from flask import Flask ,url_for, render_template

app = Flask(__name__, static_folder='assets', static_url_path='/assets')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/availability')
def availability():
    return render_template('availability.html')

if __name__ == '__main__':
    app.run(debug=True)