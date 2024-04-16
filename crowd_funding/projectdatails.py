import re
def projTitle():
    while True:
        title=input('please enter the project title')
        if title=="":
            print('title field is required')
        else:
            return title
            break

def projDetail():
    while True:
        details=input('enter the project details')
        if details=="":
            print("you must add the process datails")
        else:
            return details
            break


def projTotal():
    while True:
        total=input('enter the project target')
        if not total.isdigit():
            print('total must be a valid numbar')
        else:
            return total


def getdate(message='enter the start date as  (YYYY-MM-DD): '):
    regex=r'^\d{4}-\d{2}-\d{2}$'
    date_str = input(message)

    while not(re.fullmatch(regex,date_str)):
       # user_date = datetime.strptime(date_str, "%Y-%m-%d")
         print("Invalid date format. Please enter in YYYY-MM-DD format.")
         date_str=input('enter a valid date')
         print("You entered:", date_str)

    return date_str






