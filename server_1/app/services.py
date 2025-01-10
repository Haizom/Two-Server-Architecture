from .models import User
from .utils import load_user_db, save_user_db
import uuid
import bcrypt  


def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hashed_password, password):
    """Check a password against a stored hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def add_user_service(name, email, age, password):
    users = load_user_db()

    if any(user["email"] == email for user in users.values()):
        return {"error": "User with this email already exists"}, 400

    uid = str(uuid.uuid4())  # Generate a unique ID
    hashed_password = hash_password(password)  # Hash the password
    user = User(uid=uid, name=name, email=email, age=age, password=hashed_password.decode('utf-8'))
    users[uid] = user.to_dict()
    save_user_db(users)

    return {"message": "User added successfully", "user": users[uid]}, 201


def get_user_service(uid):
    users = load_user_db()

    if uid not in users:
        return {"error": "User not found"}, 404

    return users[uid], 200


def update_user_service(uid, age):
    users = load_user_db()

    if uid not in users:
        return {"error": "User not found"}, 404

    users[uid]['age'] = age
    save_user_db(users)

    return {"message": "User updated successfully", "user": users[uid]}, 200


def delete_user_service(uid):
    users = load_user_db()

    if uid not in users:
        return {"error": "User not found"}, 404

    del users[uid]
    save_user_db(users)

    return {"message": "User deleted successfully"}, 200


def login_user_service(email, password):
    users = load_user_db()

    user = next((user for user in users.values() if user['email'] == email), None)
    
    if not user:
        return {"error": "User not found"}, 404


    if check_password(user['password'], password):
        return {"message": "Login successful", "user": user}, 200
    else:
        return {"error": "Invalid password"}, 400
