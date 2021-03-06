from flask import Blueprint, jsonify, request, g
from models.user import User, UserSchema
from lib.helpers import is_unique
from lib.secure_route import secure_route

api = Blueprint('auth', __name__)
user_schema = UserSchema()

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user, errors = user_schema.load(data)

    if not is_unique(model=User, key='username', value=data['username']):
        errors['username'] = errors.get('username', []) + ['Username already taken']

    if not is_unique(model=User, key='email', value=data['email']):
        errors['email'] = errors.get('email', []) + ['email already taken']

    if errors:
        return jsonify(errors), 422

    user.save()

    return jsonify({'message': 'Registration Succesful'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.validate_password(data.get('password', '')):
        return jsonify({'message': 'Unauthorised'}), 401

    return jsonify({
        'message': 'Welcome back {}!'.format(user.username),
        'token': user.generate_token()
    })

@api.route('/user', methods=['GET'])
@secure_route
def profile():
    return user_schema.jsonify(g.current_user), 200
