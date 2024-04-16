import  createproject
import  projectdatails
def addproj(projectdata):
    projectdata = projectdata.strip(" \n")
    projectdata = f"{projectdata}\n"
    try:
        with open('projects.txt','a') as project:
            project.write(projectdata)
            return True
    except Exception as e:
        return False