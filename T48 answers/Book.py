class Book():
    def __init__(self, id, title, author, qty):
        '''class constructor'''
        self.id = id
        self.title = title
        self.author = author
        self.qty = int(qty)

    def set_id(self, id):
        '''ID setter'''
        self.id = id

    def set_title(self, title):
        '''Title setter'''
        self.title = title

    def set_author(self, author):
        '''Author setter'''
        self.author = author

    def set_qty(self, qty):
        '''Qty setter'''
        self.qty = int(qty)

    def dbo(self):
        '''returns tuple for DB'''
        return (self.id, self.title, self.author, self.qty)

    def __str__(self):
        '''print representation for class'''
        return (f"Book ID: {self.id}\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Quantity: {self.qty}\n")