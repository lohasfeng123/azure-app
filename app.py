from flask import Flask
import os


app = Flask(__name__)
@app.route('/')
def hello_world():
    get_env=os.popen("echo APP_ENV var is \=\=\> $AAA")
    return get_env.read()


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port=8080)

