class User():
    def __init__(self, first_name, surname, email, password,):
        self.name = first_name
        self.surname = surname
        self.email = email
        self.password = password

    def check_email(self, email):
        if "@" in email:
            return True
        else:
            return False


    def check_password(self, password):
        valid = False
        u = 0
        l = 0
        n = 0
        for character in password:
           if character.isupper():
               u += 1

           if character.islower():
                l += 1

           if character.isdigit():
               n += 1

        if u >= 1 and l >= 1 and n >=1 and len(password) <= 12 and len(password) >= 6:
            valid = True

        return valid







User1 = User("Archie", "Wright", "arch@gmail.com", "Arch1233")
print(User1.check_email(User1.email))
print(User1.check_password(User1.password))