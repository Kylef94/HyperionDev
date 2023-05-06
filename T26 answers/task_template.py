#=====importing libraries===========
from datetime import date
from Task import Task
import os

def reg_user(user):
    """handles user registration"""

    # check if admin, if not send back to main menu
    if user != "admin":
        return "You do not have permission to register users, please contact your administrator"

    # get new user details, ensure username is lower to avoid issues with matching strings at login
    new_username = input("Please enter a user name for the new user: ").lower()
    # check user has not entered nothing
    if new_username == '':
        return "You have entered nothing! Please try again"

    # check if username already registered
    if new_username in users:
        return "A user with this username is already registered!"

    new_password = input("Please enter the new users password")

    # check user has not entered nothing
    if new_password == '':
        return "You have entered nothing! Please try again"

    pass_conf = input("Please re-enter the new users password to confirm")

    # if passwords don't match take user back to main menu to try again
    if new_password != pass_conf:
        return "The passwords you entered do not match! Please try again"

    else:  # write user to users.txt
        with open("user.txt", 'a') as file:
            user = (f"{new_username}, {new_password}")
            file.write('\n')
            file.write(user)
            return f"User {new_username} has been registered!"

def add_task():
    # collect data on new task from user
    task_username = input("Please enter the user name to whom the task should be assigned: ").lower()
    #check valid user
    if task_username not in users:
        return "This user does not exist!"

    #get task info
    title = input("Please enter a title for the task: ").capitalize()
    description = input("Please enter a description of the task to be completed: ").capitalize()
    due_date = input("Please enter a due date for the task in YYYY-MM-DD format: ")
    year, month, day = map(int, due_date.split('-'))
    due_date = date(year, month, day)
    today = date.today()

    # create new task
    task = Task(task_username, title, description, today, due_date)

    task_list.append(task)
    save_tasks()
    return "task successfully added!"

def save_tasks():
    # add to tasks.txt amd confirm to user
    to_save = [task.to_file() for task in task_list]
    with open("tasks.txt", 'w') as file:
        for task in to_save:
            file.writelines(task)
        return "Tasks have been saved!"

def view_my_tasks():
    # set flag for output if no tasks assigned
    has_tasks = False

    for i, task in enumerate(task_list):
        # only output task if user has been assigned that task
        if task.assignee == user:
            has_tasks = True
            print(f"Task id: {i}")
            print(task)

    # prints output if no tasks assigned
    if not has_tasks:
        return "You do not currently have any assigned tasks!"
    else:
        edit_option = input("Please enter a task number to edit or update your task, or enter -1 to return to main menu")

        if edit_option == '-1':
            return
        else:
            edit_task(int(edit_option))

def edit_task(index):
    '''handles editing tasks'''

    #handles out of bounds index
    if index not in range(len(task_list)):
        return "Error, invalid index entered"

    task = task_list[index]
    #chck if task completed as users cannot edit complete tasks
    if task.complete:
        return "This task has already been completed, and can no longer be edited"

    #ask user what they want to change and handle appropriately
    edit_option = input("Would you like to 1) mark the task as complete; or\n 2) edit the username; or\n 3) change the due date ")

    #mark task complete
    if edit_option == '1':
        task.mark_complete()
    #edit task username
    elif edit_option == '2':
        new_user = input("Please enter which username the task should be assigned to")
        if new_user not in users:
            return "The username was not found, please try again"
        else:
            task.update_user(new_user)
    #edit due date
    elif edit_option == '3':
        due_date = input("Please enter a due date for the task in format YYYY-MM-DD: ")
        year, month, day = due_date.split('-')
        due_date = date(int(year), int(month), int(day))
        task.update_date(due_date)

    else:
        return "Invalid option entered"
    #save task edits to file
    save_tasks()



def view_all_tasks():
    '''shows all outstanding tasks'''
    has_tasks = False
    for i, task in enumerate(task_list):
        has_tasks = True
        print(f"Task id: {i}")
        print(task)

    # prints output if no tasks assigned
    if not has_tasks:
        return "There are no tasks!"
    else:
        #ask user if they want to edit task or go back to menu
        edit_option = input("Please enter a task number to edit or update a task, or enter -1 to return to main menu")

        if edit_option == '-1':
            return
        else:
            edit_task(int(edit_option))

def view_stats(user):
    '''generates user statistics'''
    # if user isnt admin send back to main menu
    if user != "admin":
         return "Only the admin can view statistics"


    # set variables for user and task counts
    num_users = 0
    num_tasks = 0
    # count users in users.txt
    with open("user.txt", 'r') as file:
        data = file.readlines()
        for line in data:
            num_users += 1

    # count tasks in tasks.txt
    with open("tasks.txt", 'r') as file:
        data = file.readlines()
        for task in data:
            num_tasks += 1

    # output to user
    return (f"Statistics: \n"
          f"Number of users: {num_users}\n"
          f"Number of tasks: {num_tasks}")

def generate_task_overview():
    '''generates task overview file'''
    #variables for task counts
    total_tasks = len(task_list)
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0

    for t in task_list:
        #check if task completed
        if t.complete:
            complete_tasks += 1
        else:
            incomplete_tasks += 1
            #logic to parse data and compare due date if task not already complete
            year, month, day = t.due_date.split('-')
            task_dd = date(int(year), int(month), int(day))
            #if due date less than todays date then it is after due date, and task is not overdue
            if task_dd > date.today():
                overdue_tasks += 1
    # % calculations
    overdue_pct = (overdue_tasks / total_tasks ) * 100 if total_tasks > 0 else 0
    incomplete_pct = (incomplete_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    #generate string output for file
    output =  f"Total tasks: {total_tasks}\n" \
           f"Completed tasks: {complete_tasks}\n" \
           f"Overdue tasks: {overdue_tasks}\n" \
           f"% tasks outstanding: {incomplete_pct}%\n" \
           f"% tasks overdue: {overdue_pct}%\n"

    #write to file
    with open("task_overview.txt", 'w') as f:
        f.write(output)

def generate_user_overview():
    '''generates user overview report'''

    total_tasks = len(task_list)
    output = []
    #iterate through registered users (as per users dict where key is username)
    for user in users.keys():
        total_user_tasks = 0
        compl_user_tasks = 0
        overdue_user_tasks = 0

        #iterate through tasks and count
        for task in task_list:
            if task.assignee == user:
                total_user_tasks += 1

            if task.assignee == user and task.complete:
                compl_user_tasks += 1

            year, month, day = task.due_date.split('-')
            task_dd = date(int(year), int(month), int(day))

            if task.assignee == user and not task.complete and (task_dd > date.today()):
                overdue_user_tasks += 1
        #handles user tasks being equal to 0, which would cause ZeroDivisionError for %'s if user tasks is 0
        if total_user_tasks == 0:
            output.append(f"User: {user}\n" 
                 f"Total user tasks: 0\n" 
                 f"% of tasks assigned to user: 0%\n" 
                 f"% user tasks completed: 0%\n" 
                 f"% user tasks to complete: 0%\n" \
                 f"% user tasks overdue: 0%\n" 
                 f"\n")
        else:
            output.append(f"User: {user}\n" 
                     f"Total user tasks: {total_user_tasks}\n" 
                     f"% of tasks assigned to user: {(total_user_tasks / total_tasks) * 100}%\n" 
                     f"% user tasks completed: {(compl_user_tasks / total_user_tasks) * 100}%\n" 
                     f"% user tasks to complete: {((total_user_tasks - compl_user_tasks) / total_user_tasks) * 100}%\n" \
                     f"% user tasks overdue: {(overdue_user_tasks / total_user_tasks) *100}%\n" 
                     f"\n")
    #write to file
    with open("user_overview.txt", "w") as f:
        for o in output:
            f.write(o)






#====Login Section====
#set up dictionary to store registered users for login checks and var to store logged in users name
users = {}
user = str()

#pull user data from file and add to users dictionary
with open("user.txt", 'r') as file:
    data = file.readlines()
    for user in data:
        username, password = user.split(", ")
        password = password.strip('\n')
        users.update({username: password})

#setup task list
task_list = []

#load existing tasks
with open("tasks.txt", 'r') as file:
    tasks = file.readlines()
    for task in tasks:
        # iterate through tasks and split into data which can be output to user
        assignee, title, desc, assigned_date, due_date, completed_flag = task.split(", ")
        completed_flag = completed_flag.strip()
        task = Task(assignee, title, desc, assigned_date, due_date, completed_flag)
        task_list.append(task)

#set flag for while loops
logging_in = True

#loops until logged in successfully
while logging_in:
    username = input("Please enter your username").lower()
    #checks if user registered
    if username not in users:
        print("Error: invalid username entered, please enter a registered user name")
        continue

    password = input("Please enter your password")

    #log user in
    if password == users[username]:
        user = username
        print(f"Logged in as {user}")
        logging_in = False
    else: #restart loop if invalid details entered
        print("Error: invalid password")


while not logging_in:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if user == "admin":
        menu_text = '''Select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    s - statistics
    e - Exit
    : '''
    else:
        menu_text = '''Select one of the following options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : '''
    menu = input(menu_text).lower()

#logic for menu options

    #register user
    if menu == 'r':
        reg_user(user)

    #add task
    elif menu == 'a':
        add_task()

    #view all tasks
    elif menu == 'va':
        view_all_tasks()

    #view my tasks
    elif menu == 'vm':
        view_my_tasks()

    #statistics option for admin only
    elif menu == 's':
        view_stats(user)

    elif menu == 'gr':
        #check if reports exist, if not then generate before displaying
        if not os.path.exists("/user_overview.txt"):
            generate_user_overview()

        if not os.path.exists("/task_overview.txt"):
            generate_task_overview()

        #print user overview
        with open("user_overview.txt", "r") as f:
            data = f.read()
            print("User Overview")
            print(data)

        #print task_overview
        with open("task_overview.txt", "r") as f:
            data = f.read()
            print("Task Overview")
            print(data)

    #exit option
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    #invalid option entered
    else:
        print("You have made a wrong choice, Please Try again")