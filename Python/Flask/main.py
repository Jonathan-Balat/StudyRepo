from flask import Flask

# Pass Python's special variable to Flask, allowing the latter to setup with the right paths and configurations.
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
# WRAP UP:
# - Don't forget to activate venv
# - pip freeze > requirements.txt