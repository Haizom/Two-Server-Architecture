import bcrypt

class User:
    def __init__(self, uid, name, email, age, password):
        self.uid = uid
        self.name = name
        self.email = email
        self.age = age
        self.password = password  

    def to_dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "password": self.password
        }
