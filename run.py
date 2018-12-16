from flask import Flask, jsonify, request

app = Flask(__name__)
questions = {}
users = {}


@app.route('/')
def home():
    '''
    home
    '''
    return "Hallo API"


@app.route('/questions', methods=['GET'])
def all_questions():
    return jsonify({'questions': questions})


@app.route('/question/<int:question_id>', methods=['GET'])
def question(question_id):
    question = questions.get(question_id)
    if not question:
        return jsonify({"message": "No question matching that ID"})
    else:
        return jsonify({'question': question})


@app.route('/questions/add', methods=['GET', 'POST'])
def create():
    '''adding new questions'''
    stuff = request.get_json()
    if not stuff:
        return jsonify({"message": "Data set cannot be empty"})
    title = stuff.get('title')
    content = stuff.get('content')
    question_id = len(questions)
    questions[question_id] = {
        'question_id': question_id, 'title': title, 'content': content}
    return 'Added content'


@app.route('/signup', methods=['POST'])
def register_user():
    '''endpoint to create an account'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"})
    email_address = data.get('email_address')
    username = data.get('username')
    password = data.get('password')
    user_id = len(users)

    users[user_id] = {'user_id': user_id, 'email_address': email_address,
                      'username': username, 'password': password}

    return jsonify({'users': users})


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/question/<int:question_id>', methods=['DELETE'])
def delete(question_id):
    question = questions.get(question_id)

    if not question:
        return jsonify({"message": "No question matching that ID"})
    else:
        discard = questions.pop(question_id)
        return jsonify({"message": "Question matching that ID has been deleted"})


if __name__ == '__main__':
    app.run(debug=True)
