class User:
  
  # Constructor
  def __init__(self, user_id, username):
    # Initialise attributes
    self.id = user_id
    self.username = username
    self.followers = 0 # default value
    self.following = 0 # default value
  
  # Methods
  def follow(self, user):
    user.followers += 1
    self.following += 1
  
  def recap(self):
    print(f"Follower {self.username}: {self.followers}")
    print(f"Following {self.username}: {self.following}")


user_1 = User(username="Budi", user_id=1)
user_2 = User(2, "Siti")

user_1.follow(user_2)

user_1.recap()
user_2.recap()
