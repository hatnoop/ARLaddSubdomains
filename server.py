from flask import Flask, request
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = '6fGuJdMGjN4tu1y'
basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def index():
    domain = request.args.get('domain')
    filename = domain + '.txt'
    with open(filename, 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9988')