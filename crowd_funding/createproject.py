import projectdatails
import addproject
import register
import projectnanipulate
import adduser
import general
def creatProject():
    title=projectdatails.projTitle()
    details=projectdatails.projDetail()
    target=projectdatails.projTotal()
    sdate=projectdatails.getdate()
    edate=projectdatails.getdate('enter the end date as  (YYYY-MM-DD): ')
    owner_id=general.static_id
    prepared=f"{title}:{details}:{target}:{sdate}:{edate}:{owner_id}"
    savedproject=addproject.addproj(prepared)
    print('your project has been added successfully ')


def menu():
    while True:
        print("\nplease select what you want to do :")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search for project")
        print("6. Exit")
        choice=input('enter your choice ')
        if choice=='1':
            creatProject()
        elif choice=='2':
            projectnanipulate.view()
        elif choice=='3':
            projectnanipulate.edit()
        elif choice=='4':
            projectnanipulate.delete()
        elif choice=='5':
            projectnanipulate.search()
        elif choice=='6':
            print('**** goodbye **** ')
            break
        else:
            print('invalid choice please enter a number between 1 and 5')