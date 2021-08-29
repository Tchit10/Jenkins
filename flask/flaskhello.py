from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world with Jenkins and my Github Repo !!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
