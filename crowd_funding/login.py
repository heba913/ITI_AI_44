import createproject
import general


def login():
    email=input('enter your email')
    password=input('enter your password')
    with open("users.txt", "r") as file:
        while True:
            for line in file:
                user_data = line.split(':' )
                if user_data[2] == email and user_data[3] == password:
                    user_id=user_data[5]
                    general.static_id=user_id
                    print(f"\nLogin successful .welcome , {user_data[0]} ")
                    return True
                print("Login failed Invalid email or password")





