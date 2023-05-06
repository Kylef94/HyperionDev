import sqlite3
from Book import Book

db = sqlite3.connect("ebookstore.db")

cur = db.cursor()

#CREATE TABLE
def create_books_table():
    '''creates table called books in DB'''
    try:
        cur.execute(
            "CREATE TABLE books(id char(4) unique not null, title varchar(30) not null, author varchar(30) not null, qty int(10) not null)")
        db.commit()

    except sqlite3.OperationalError:
        print("Books table already exists!")

#ADD, DELETE, UPDATE METHODS

def add_book():
    '''adds a book to the DB'''

    id = input("Please enter the book id")

    # data integrity check
    if len(id) > 4:
        print("id provided does not match required format! please ensure id is max 4 characters long")
        return

    title = input("Please enter the book title")
    # data integrity check
    if len(title) > 30:
        print("title provided does not match required format! please ensure title is max 30 characters long")
        return

    author = input("Please enter the book author")
    # data integrity check
    if len(author) > 30:
        print("author provided does not match required format! Please ensure author is max 30 characters long")
        return

    qty = input("Please enter the book quantity")

    if not qty.isnumeric():
        print("Error: the quantity you entered contained letters, please only enter whole numbers for the quantity")
        return

    try:
        cur.execute("insert into books values(?, ?, ?, ?)", (id, title, author, int(qty)))
        db.commit()
        print(f"book {title} has been added to the database")

    except sqlite3.IntegrityError:
        print(f"Could not add {title} to DB as a duplicate record was found, please check and try again")


def delete_book():
    '''Deletes a book from the DB'''

    id = input("Please enter the id of the book you would like to delete, or enter nothing to return to main menu")

    if id == '':  # return to main menu
        print("Returning to main menu")
        return

    # find book
    try:
        book = find_book_id(id)
    except LookupError:
        print("Error: book could not be found, please try again")
        return

    # confirm delete with user
    delete_confirm = input("This book will be permanently deleted, please confirm (y/n)").capitalize()

    if delete_confirm == 'Y':
        cur.execute("delete from books where id = ?", (id,))
        db.commit()
        print("book deleted!")
    else:  # if user chooses not to delete
        print(f"{book.title} has not been deleted")


def update_book():
    '''updates book record in DB based on user inputs'''

    id = input("Please enter the id of the book you would like to update, or enter nothing to return to main menu")

    if id == '':
        print("Returning to main menu")
        return

    # find book
    try:
        book = find_book_id(id)

    except LookupError:
        print("Error: book could not be found, please try again")
        return

    # change title
    new_title = input("Please enter the new title, or leave blank and hit enter to skip")

    if len(new_title) > 30:
        print("title provided does not match required format! please ensure title is max 30 characters long")

    elif new_title != '':
        book.set_title(new_title)

    # change author
    new_author = input("Please enter the new author, or leave blank and hit enter to skip")

    if len(new_author) > 30:
        print("author provided does not match required format! Please ensure author is max 30 characters long")

    elif new_author != '':
        book.set_author(new_author)

    # change qty
    new_qty = input("Please enter the new quantity, or leave blank and hit enter to skip")

    if new_qty != '':
        if not new_qty.isnumeric():
            print("Error: the quantity you entered contained letters, please only enter whole numbers for the quantity")
            return
        else:
            book.set_qty(new_qty)

    # update record by id
    id, title, author, qty = book.dbo()
    cur.execute("update books set title = ? where id = ? ", (title, id))
    cur.execute("update books set author = ? where id = ? ", (author, id))
    cur.execute("update books set qty = ? where id = ? ", (qty, id))
    db.commit()

    # confirm to user
    print("The record has been updated, it is now as follows:\n")
    print(book)


#FINDING BOOKS

def find_book_id(id):
    ''''finds a book in the DB using ID'''

    cur.execute("select * from books where id = ?", (id,))
    book_record = cur.fetchone()

    if not book_record:  # if book not found
        raise LookupError(f"Could not "
                          f"find book {id}")

    # output
    id, title, author, qty = book_record
    book = Book(id, title, author, qty)
    print("Found book:")
    print(book)
    return book


def find_book_title(title):
    ''''finds a book in the DB using title'''

    # set string for lookup
    title = f'%{title}%'
    cur.execute("select * from books where title like ?", (title,))
    book_records = cur.fetchall()

    if not book_records:  # book not found
        raise LookupError(f"Could not find book with title containing {title}")

    print(f"Found {len(book_records)} book(s):")

    # output to user
    for book in book_records:
        id, title, author, qty = book
        print(Book(id, title, author, qty))


def find_book_author(author):
    ''''finds a book in the DB using author'''

    # set string for cursor
    author = f'%{author}%'

    cur.execute("select * from books where author like ?", (author,))
    book_records = cur.fetchall()

    if not book_records:
        return LookupError(f"Could not find book with title containing {author}")

    print(f"Found {len(book_records)} book(s):")
    # iterate through results and print
    for book in book_records:
        id, title, author, qty = book
        print(Book(id, title, author, qty))


def search_books():
    '''handles menu for searching books in DB'''
    choice = input("Please select how you would like to search for books:\n"
                   "1) by ID\n"
                   "2) by title\n"
                   "3) by author\n")

    match choice:
        case '1':  # ID Search
            id = input("Please enter the id you would like to search for")
            try:
                find_book_id(id)

            except LookupError:
                print(f"Could not find book with id {id}")

        case '2':  # title search
            title = input("Please enter the title you would like to search for (partial titles are possible)")
            try:
                find_book_title(title)

            except LookupError:
                print(f"Could not find book with title {title}")

        case '3':  # author search
            author = input("Please enter the author name you would like to search for (partial names are possible)")
            try:
                find_book_author(author)
            except LookupError:
                print(f"Could not find book with author  {author}")

def get_all_books():
    '''returns all books in the DB'''
    cur.execute("select * from books")
    books = cur.fetchall()
    print(f"Database currently has {len(books)} books")
    for book in books:
        id, title, author, qty = book
        print(Book(id, title, author, qty))


def main():
    '''main loop'''
    print("Ebookstore")

    # loops until exit

    user_option = '0'
    while user_option:
        user_option = input("Please select from the options below(enter the number as appropriate:\n"
                            "1) add a book\n"
                            "2) delete a book\n"
                            "3) update a book record\n"
                            "4) search for books\n"
                            "5) get all books\n"
                            "6) Exit\n")

        match user_option:
            case '1':  # add a book to DB
                add_book()

            case '2':  # delete book from DB
                delete_book()

            case '3':  # update book
                update_book()

            case '4':  # search books
                search_books()

            case '5': #get all books
                get_all_books()

            case '6':  # exit
                exit(0)

            case _:  # other
                print("Invalid option entered, please try again entering only the digit for the option you require")


if __name__ == "__main__":
    # code to set up table and db entries
    # create_books_table()
    # id_list = ['3001', '3002', '3003', '3004', '3005']
    # title_list = ['A Tale of Two Cities', "Harry Potter and the Philosophers Stone", "The Lion, the Witch, and the Wardrobe", "The Lord of the Rings", "Alice in Wonderland"]
    # author_list = ['Charles Dickens', 'J.K Rowling', 'C.S Lewis', 'J.R.R Tolkien', "Lewis Carroll"]
    # qty_list = [30, 40, 25, 37, 12]
    #
    # for i in range(len(id_list)):
    #     cur.execute("insert into books values(?, ?, ?, ?)", (id_list[i], title_list[i], author_list[i], qty_list[i]))
    #     db.commit()
    #     print(f"added {title_list[i]}")

    main()
