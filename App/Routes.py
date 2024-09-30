from flask import request, jsonify
from app import app, bcrypt
from app.models import User, File
from app.auth import authenticate_user
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(data['email'], hashed_password, 'client')
    user.save_to_db()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate_user(data['email'], data['password'])
    if token:
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    current_user = get_jwt_identity()
    if current_user['user_type'] != 'ops':
        return jsonify({'message': 'Unauthorized'}), 403
    # Handle file upload logic here
    return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download/<file_id>', methods=['GET'])
@jwt_required()
def download_file(file_id):
    current_user = get_jwt_identity()
    if current_user['user_type'] != 'client':
        return jsonify({'message': 'Unauthorized'}), 403
    # Generate and return secure download link
    return jsonify({'download-link': 'secure_link', 'message': 'success'}), 200
  
