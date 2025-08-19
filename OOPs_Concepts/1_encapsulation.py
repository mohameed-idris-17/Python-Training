# Example B: User Authentication System (Encapsulation)
# What’s being encapsulated: the user’s credentials (username, password) and the logic for verifying or changing them.
# What’s hidden: direct access to the raw password and username; they can’t be read or modified from outside the class.
# What’s exposed: safe actions like login and change_password that enforce authentication rules.
# How it works conceptually: all credential checks and updates must go through these methods, ensuring only valid operations are allowed.
# Why it matters: protects sensitive data, prevents unauthorized access or tampering, and centralizes security logic.
# One-liner for interview: “Encapsulation keeps credentials private and only allows changes or checks through secure, rule-enforcing methods.
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
