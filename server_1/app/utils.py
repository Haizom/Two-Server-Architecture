import json

def load_user_db():
    try:
        with open('users.txt', 'r') as f:
            content = f.read()
            if not content:
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_user_db(users):
    with open('users.txt', 'w') as f:
        json.dump(users, f)
