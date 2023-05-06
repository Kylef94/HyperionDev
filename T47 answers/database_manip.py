import sqlite3

#set up db and cursor
db = sqlite3.connect('exampledb')

cursor = db.cursor()

#create table
# cursor.execute("CREATE TABLE python_programming("
#                "id CHAR(4),"
#                "name CHAR(30),"
#                "grade INT(2))")
# db.commit()

#add records to table

# id_list = ['55', '66', '77', '12', '2']
# name_list = ['Carl Davis', 'Dennis Fredrickson', 'Jane Richards', 'Peyton Sawyer', 'Lucas Brooke']
# grade = [61, 88, 78, 45, 99]
#
# for i in range(len(id_list)):
#
#     cursor.execute("INSERT INTO python_programming VALUES (?, ?, ?)", (id_list[i], name_list[i], grade[i]))
#
# db.commit()

#select all records between 60 and 80
cursor.execute("SELECT * FROM python_programming "
               "WHERE grade BETWEEN 60 AND 80")
records = cursor.fetchall()

#change carl davis' grade

cursor.execute("UPDATE python_programming SET grade = 65 WHERE id = '55' AND name = 'Carl Davis'")
db.commit()

#delete dennis' row
name = ('Dennis Fredrickson',)
cursor.execute("DELETE FROM python_programming WHERE name = ?", name )
db.commit()

#change grade of all ppl with id below 55

cursor.execute("UPDATE python_programming SET grade = ? WHERE id < ?", (100, '55'))
db.commit()


db.close()








