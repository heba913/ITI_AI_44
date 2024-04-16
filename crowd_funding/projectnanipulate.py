import time
import register
import general
import createproject

def view():
    with open('projects.txt','r')as projects:
        for line in projects:
            print(line)
            time.sleep(1)




# def edit ():
#     with open('projects.txt', 'r') as proj_f:
#          p_contents = proj_f. readlines()
#          for index, row in enumerate(p_contents):
#             print('lines')
#             project = row.strip().split(":")
#             print('splitted')
#             if project[5] == general.static_id:
#                 print('configuration')
#                 print ("Project was found")
#                 print("Please enter your modifications")
#                 for index, row in enumerate(p_contents):
#                     p = row.strip.split(" :")
#                     p_contents[index] = createproject.creatProject()
#
#                 break
#          else:
#             print("project not found")
#             return 0

# def edit():
#     with open('projects.txt', 'r+') as projects:
#         while True:
#             line = projects.readlines()
#             for index,row in enumerate(line) :
#                 pro_data=row.split(':')
#                 if pro_data[5] == general.static_id:
#                     print(pro_data)
#                     time.sleep(1)
#                     print('enter your modification please ')
#                     pro_data[index]=createproject.creatProject()
#                     return
#                 else:
#                     print('no projects')
    #
def edit():
    with open('projects.txt' ,'r') as file:
        lines = file.readlines()
        project_found = False
        for i, line in enumerate(lines):
            if general.static_id in line:
                project_found = True
                print("Current Project Details:")
                print(line)
                newTitle = input("Enter the new project title: ")
                newDetaile=input("Enter the nee  prpject details")
                newTarget = input("Enter the new project target: ")
                new_start_date = input("Enter the new project start date (YYYY-MM-DD): ")
                new_end_date = input("Enter the new project end date (YYYY-MM-DD): ")
                lines[i] = f"{newTitle}:{newDetaile}:{newTarget}:{new_start_date}:{new_end_date}:{general.static_id}"
                with open('projects.txt', 'w') as file:
                    file.writelines(lines)
def delete():
    with open('projects.txt', 'r') as file:
        lines = file.readlines()
        project_found = False
        for i, line in enumerate(lines):
            if general.static_id in line:
                project_found = True
                del lines[i]
                break

    with open('projects.txt', 'w') as file:
        file.writelines(lines)

    if project_found:
        print(f"Project with ID {general.static_id} is deleted .")
        time.sleep(.5)
    else:
        print(f"no project with the id {general.static_id} .")
        time.sleep(.5)








# def search():
#     while True:
#         with open('projects.txt', 'r') as projects:
#             for line in projects:
#                 project_data = line.split(':')
#                 project_title=input('please enter the title of the project')
#                 if project_data[0] == project_title:
#                     print(line)
#                     time.sleep(.5)
#                     return 1
#                 else:
#                     print("no projects with this title ")


def search():
    with open('projects.txt', 'r') as file:
        lines = file.readlines()
        matching_projects = []
        target_title=input('enter the prokect title')
        for line in lines:
            project_data = line.strip().split(':')
            project_title = project_data[0]
            if target_title.lower() in project_title.lower():
                matching_projects.append(line)
        if matching_projects:
            print(f"Projects with title '{target_title}':")
            for project in matching_projects:
                print(project)
                time.sleep(.5)
        else:
            print(f"No projects found with title '{target_title}'.")



