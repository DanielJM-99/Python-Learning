# Create a class

class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        # Default attribute
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("007", "Daniel Craig")
print(user_1.id)
user_2 = User("001", "Angelina Jolie")
print(user_2.id, user_2.user_name, user_2.followers)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
