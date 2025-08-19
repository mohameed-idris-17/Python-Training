# Example B: User Authentication System (Encapsulation)
class UserAuth:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if username == self.__username and password == self.__password:
            return "Login Successful"
        return "Invalid Credentials"

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return "Password Changed Successfully"
        return "Incorrect Old Password"

auth = UserAuth("admin", "1234")
print(auth.login("admin", "1234"))
print(auth.change_password("1234", "abcd"))
print(auth.login("admin", "abcd"))
