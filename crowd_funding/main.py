import register
import login
import  createproject

print('****** welcome in crowd funding  *******')
selection=input('please enter 1 for registration  or 2 for login')
if selection =='1':
    register.register()
elif selection == '2':
    login.login()
    createproject.menu()
