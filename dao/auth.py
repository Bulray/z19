class AuthDAO:

    def __init__(self, session):
        self.session = session


    def create(self, data):
        auth = User(**data)
        self.session.add(Auth)
        self.session.commit()
        return auth



    def get_by_username(self, username):
      return {
          'username': 'test',
          'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
          'role': 'user',
    }