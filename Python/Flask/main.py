from flask import Flask, render_template

# Pass Python's special variable to Flask, allowing the latter to setup with the right paths and configurations.
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

# NOTE: No need to specify "template/" path, this is already visible to Flask.
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# WRAP UP:
# - Don't forget to activate venv
# - pip freeze > requirements.txt