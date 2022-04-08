from dao.models.user import User
#CRUD

class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return session.query(User).all()



    def get_one(self, bid):
        return self.session.query(User).get(bid)



    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.name = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get('role')

        self.session.add(user)
        self.session.commit()
        return user

    def create(self, data):
        user = User(**data)
        self.session.add(User)
        self.session.commit()
        return user


    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

