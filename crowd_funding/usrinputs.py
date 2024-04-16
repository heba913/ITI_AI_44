import re

def getname(message="please enter your frist name"):
    while True:
        name=input(message)
        if name.isalpha():
            return name
        else:
            print("error input")


def getEmail(message="please enter your email"):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email = input(message)
        while not (re.fullmatch(regex, email)):
            print("inValid Email")
            email = input(message)
            print("valid Email")
        return email

def get_password():
    while True:
        try:
            password = input("Please enter your password: ")
            if len(password) >= 6:
                print('password entered')
                newpass = input('confirm password')
                if password == newpass:
                    print('password confirmed')
                else:
                    newpass = input(' password do not match')
                return password

            else:
                raise ValueError("Error: Password must be at least 6 characters.")
        except ValueError as e:
            print(e)



def validate_phone(message='please enter your phone'):
     phone=input(message)
     regex=r"01[0-6]\d{8}"
     while not(re.fullmatch(regex,phone)):
         print('phone not validated')
         phone=input(message)
     print('phone validated')
     return phone










