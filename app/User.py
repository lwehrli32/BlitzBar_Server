class UserRepository:

    def __int__(self):
        self.users = {}

    def add_user(self):
        pass


class User:

    def __init__(self, first_name, last_name, email, radius):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.radius = radius
        self.email = email
        self.blitz_score = 0
