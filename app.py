from flask import Flask
import os


app = Flask(__name__)
@app.route('/')
def hello_world():
    get_env=os.popen("echo $HOSTNAME")
    return get_env.read()

