from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/hello/<name>')
def hello(name):
    return f"{name}, hello world"

if __name__ =="__main__":
    app.run()