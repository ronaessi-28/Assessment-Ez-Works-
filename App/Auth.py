from app import bcrypt, jwt
from flask_jwt_extended import create_access_token

def authenticate_user(email, password):
    user = User.find_by_email(email)
    if user and bcrypt.check_password_hash(user['password'], password):
        return create_access_token(identity={'email': user['email'], 'user_type': user['user_type']})
    return None
  
