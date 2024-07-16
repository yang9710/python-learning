class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
def sort_notcompare():
    print(users)
    print(sorted(users, key=lambda u: u.user_id))

sort_notcompare()


# 使用 attrgetter faster than lambda
from operator import attrgetter
sorted(users, key=attrgetter('user_id'))