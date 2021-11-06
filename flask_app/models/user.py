from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []

        for y in results:
            users.append(cls(y))
        return users


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(fname)s, %(lname)s, %(email)s);"
        results = connectToMySQL('users_schema').query_db(query,data)
        return 

    @classmethod
    def show(cls):
        query = "SELECT * FROM users WHERE id= %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id= %(id)s"
        user = connectToMySQL('users_schema').query_db(query,data)
        return cls(user[0])


    @classmethod
    def edituser(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s WHERE id= %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id= %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

