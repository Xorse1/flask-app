from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask Python! We are building an automatic deployment to AWS using codepipeline"


if __name__ == '__main__':
    app.run(debug=True)