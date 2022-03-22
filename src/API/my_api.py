from flask import Flask, jsonify, request

port_server = 5000
app = Flask(__name__)

users = [
    {
        "nume": "Andrei",
        "email": "andreihustiuc@yahoo.com"
    },
    {
        "nume": "Andrei",
        "email": "andreihustiuc@yahoo.com"
    },
    {
        "nume": "Andrei",
        "email": "andreihustiuc@yahoo.com"
    }
]


@app.route('/')
def get_home():
    return users[0]


@app.route('/user')
def get_user():
    return jsonify({"users": users})


@app.route('/post', methods=['POST'])
def add_user():
    usr = request.get_json()
    users.append(usr)
    return 'New user added', 201


if __name__ == '__main__':
    app.run('localhost', port_server, True)
