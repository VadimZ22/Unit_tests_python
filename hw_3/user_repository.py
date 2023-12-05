class UserRepository:
    users = []

    def add_user(self, user):
        self.users.append(user)

    def all_users_logout(self):
        users_list = []
        for user in self.users:
            if user.admin:
                users_list.append(user)
        self.users = users_list
