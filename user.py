from mysqlconnection import connectToMySQL

# Watch your indentation! @classmethod goes down in line with def__init__ and the methods are in line with @classmethod!

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Class method to query the database to show all users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

    # Class method to save a new user to the database
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(eml)s);"
        return connectToMySQL('users_schema').query_db(query, data)