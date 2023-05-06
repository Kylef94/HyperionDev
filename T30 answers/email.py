class Email:

    def __init__(self, sender, contents):
        self.has_been_read = False
        self.email_contents = contents
        self.is_spam = False
        self.from_address = sender

    # set print representation
    def __str__(self):
        return f"sender: {self.from_address}\n" \
               f"email: {self.email_contents}\n" \
               f"spam: {self.is_spam}\n" \
               f"read: {self.has_been_read}"

    def mark_as_read(self):
        '''marks email as read'''
        self.has_been_read = True

    def mark_as_spam(self):
        '''marks email as spam'''
        self.is_spam = True


# set up inbox to store emails
inbox = []
outbox = []


# inbox methods

def get_count():
    '''gets total count of emails in inbox'''
    return len(inbox)


def add_email(sender, contents):
    '''adds an email to the inbox'''
    email = Email(sender, contents)
    inbox.append(email)


def get_email():
    '''retreives an email from the inbox'''
    chosen_email = input("Please enter the id of the email you would like to read, or input -1 to go back to main menu")
    if chosen_email == '-1':
        return
    else:
        chosen_email = int(chosen_email)
        if chosen_email in range(len(inbox)):
            email = inbox[chosen_email]
            print(email)
            email.mark_as_read()



def get_unread_emails():
    '''returns only unread emails from inbox'''
    for i, e in enumerate(inbox):
        if e.has_been_read == False:
            print(f'id: {i}')
            print(e)


def get_all_emails():
    '''returns all emails in inbox'''
    for i, e in enumerate(inbox):
        print(f'id: {i}')
        print(e)


def get_spam_emails():
    '''returns only spam emails in inbox'''
    for e in inbox:
        if e.is_spam == True:
            print(e)


def delete(email):
    '''deletes an email'''
    inbox.remove(email)


def get_sent_emails():
    '''gets all emails that have been sent by the user'''
    for e in outbox:
        print(e)


# An Email Simulation

user_choice = ""
# set up some emails for the app
add_email("john@google.com", "Hello")
add_email("Kyle@kyle.com", "Test")

# loops until exit
while user_choice != "quit":

    user_choice = input("What would you like to do - read/get count/mark spam/send/delete/quit?")
    # read emails
    if user_choice == "read":
        option = input("Would you like to read - all / unread / spam / sent / email")
        #output appropriate option to user
        match option:
            case 'all':
                get_all_emails()
                get_email()

            case 'unread':
                get_unread_emails()
                get_email()

            case 'spam':
                get_spam_emails()
                get_email()

            case 'sent':
                get_sent_emails()

            case 'email':
                get_email()
    #get count
    elif user_choice == "get count":
        print(f"You have {get_count()} emails in your inbox")

    # mark as spam
    elif user_choice == "mark spam":
        get_all_emails()  # display to user so they know which id to input
        index = int(input("Please enter the id of the email you would like to mark as spam: "))
        email = inbox[index]
        email.mark_as_spam()
        print("This email has been marked as spam!")
    # send an email
    elif user_choice == "send":
        to_email = input("Please enter the recipient email\n")
        content = input("Please input the emails content\n")
        email = Email(to_email, content)
        outbox.append(email)
        print("your e-mail has been sent!")

    elif user_choice == "delete":
        get_all_emails()  # display to user so they know which id to input
        index = int(input("Please enter the id of the email you would like to delete: "))
        email = inbox[index]
        delete(email)
        print("This email has been deleted!")
    # exit
    elif user_choice == "quit":
        print("Goodbye")
    # invalid input
    else:
        print("Oops - incorrect input")
