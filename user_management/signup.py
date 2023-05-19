from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy user database
users = []


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    user = {'username': username, 'password': password}
    users.append(user)

    return jsonify({'message': 'User registered successfully'}), 201


if __name__ == '__main__':
    app.run()
