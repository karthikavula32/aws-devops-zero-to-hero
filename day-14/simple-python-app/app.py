from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world v2!'

if __name__ == '__main__':
    app.run()

