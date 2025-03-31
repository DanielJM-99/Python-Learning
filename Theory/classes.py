# class User:
#     pass

# user_1 = User()
# user_1.id = "007"
# user_1.username = "Daniel Craig"

# user_2 = User()
# user_2.id = "003"
# user_2.username = "Michelle Williams"

#print(user_1.username)
#print(user_2.username)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # Init an attribute with a value
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        # User you are following gets one more follower
        user.followers += 1
        # You start following one more person
        self.following += 1

# Instead of 3 lines we got 1 with init values
user_1 = User("007", "Daniel Craig")
user_2 = User("003", "Michelle Williams")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
