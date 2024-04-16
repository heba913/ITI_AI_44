import usrinputs
import adduser
import time
def register():
    name=usrinputs.getname()
    lname=usrinputs.getname("please enter you last name")
    email=usrinputs.getEmail()
    password=usrinputs.get_password()
    phone=usrinputs.validate_phone()
    id=getid()
    prepared_data=f"{name}:{lname}:{email}:{password}:{phone}:{id}"
    saved=adduser.addUser(prepared_data)
    print(f'you are all set  <3,{name}')

def getid():
    userid = round(time.time())
    return userid


