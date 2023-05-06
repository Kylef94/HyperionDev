#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

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
        #check if admin, if not send back to main menu
        if user != "admin":
            print("You do not have permission to register users, please contact your administrator")
            continue

        #get new user details, ensure username is lower to avoid issues with matching strings at login
        new_username = input("Please enter a user name for the new user: ").lower()
        # check user has not entered nothing
        if new_username == '':
            print("You have entered nothing! Please try again")
            continue

        #check if username already registered
        if new_username in users:
            print("A user with this username is already registered!")
            continue

        new_password = input("Please enter the new users password")

        #check user has not entered nothing
        if new_password == '':
            print("You have entered nothing! Please try again")
            continue

        pass_conf = input("Please re-enter the new users password to confirm")


        #if passwords dont match take user back to main menu to try again
        if new_password != pass_conf:
            print("The passwords you entered do not match! Please try again")

        else: #write user to users.txt
            with open("user.txt", 'a') as file:
                tasks = (f"{new_username}, {new_password}")
                file.write('\n')
                file.write(tasks)
                print(f"User {new_username} has been registered!")

    #add task
    elif menu == 'a':
        #collect data on new task from user
        task_username = input("Please enter the user name to whom the task should be assigned: ").lower()
        title = new_username = input("Please enter a title for the task: ").capitalize()
        description = new_username = input("Please enter a description of the task to be completed: ").capitalize()
        due_date = new_username = input("Please enter a due date for the task: ")
        today = date.today()

        #create string for new task
        task = f"{task_username}, {title}, {description}, {due_date}, {today}, No"

        #add to tasks.txt amd confirm to user
        with open("tasks.txt", 'a') as file:
            file.write('\n')
            file.write(task)
            print(f"Task '{title}' has been registered!")

    #view all tasks
    elif menu == 'va':
        #read tasks from file
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                #iterate through tasks and split into data which can be output to user
                assignee, title, desc, assigned_date, due_date, completed_flag = task.split(", ")
                print(f"Task: {title}\n"
                      f"Assigned to: {assignee}\n"
                      f"Date assigned: {assigned_date}\n"
                      f"Due date: {due_date}\n"
                      f"Task Complete?: {completed_flag}\n"
                      f"Task Description:\n {desc}\n"
                      )
    #view my tasks
    elif menu == 'vm':
        #set flag for output if no tasks assigned
        user_tasks = False

        #read tasks
        with open("tasks.txt", 'r') as file:
            tasks = file.readlines()

            for task in tasks:
                # iterate through tasks and split into data which can be output to user
                assignee, title, desc, assigned_date, due_date, completed_flag = task.split(", ")

                #only output task if user has been assigned that task
                if assignee == user:
                    user_tasks = True
                    print(f"Task: {title}\n"
                          f"Assigned to: {assignee}\n"
                          f"Date assigned: {assigned_date}\n"
                          f"Due date: {due_date}\n"
                          f"Task Complete?: {completed_flag}\n"
                          f"Task Description:\n {desc}\n"
                          )
            #prints output if no tasks assigned
            if not user_tasks:
                print("You do not currently have any assigned tasks!")

    #statistics option for admin only
    elif menu == 's':
        #if user isnt admin send back to main menu
        if user != "admin":
            print("Only the admin can view statistics")
            continue

        #set variables for user and task counts
        num_users = 0
        num_tasks = 0
        #count users in users.txt
        with open("user.txt", 'r') as file:
            data = file.readlines()
            for user in data:
                num_users += 1

        # count tasks in tasks.txt
        with open("tasks.txt", 'r') as file:
            data = file.readlines()
            for task in data:
                num_tasks += 1

        #output to user
        print(f"Statistics: \n"
              f"Number of users: {num_users}\n"
              f"Number of tasks: {num_tasks}")


    #exit option
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    #invalid option entered
    else:
        print("You have made a wrong choice, Please Try again")