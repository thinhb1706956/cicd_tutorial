from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello FOSS'

if __name__ == '_main_':

    app.run(debug=True,host='0.0.0.0')

from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello FOSS, Hello CI/CD using Jenkins'
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
