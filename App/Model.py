from app import mongo

class User:
    def __init__(self, email, password, user_type):
        self.email = email
        self.password = password
        self.user_type = user_type

    def save_to_db(self):
        mongo.db.users.insert_one(self.__dict__)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

class File:
    def __init__(self, filename, owner_id):
        self.filename = filename
        self.owner_id = owner_id

    def save_to_db(self):
        mongo.db.files.insert_one(self.__dict__)

    @staticmethod
    def find_by_owner(owner_id):
        return mongo.db.files.find({'owner_id': owner_id})
      
