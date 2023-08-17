import sqlite3

connect = sqlite3.connect("tab1.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
connect.commit()

#connect = sqlite3.connect("tab2.db")
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
connect.commit()

l = [1, 2, 3, "apple", "orange", 35, "snow"]
for i in str(l):
    if i.isalpha():
        cursor.execute('''INSERT INTO tab1(col_1) VALUES(?)''', (i,))
        k = len(str(i))
        print(k)
        cursor.execute('''INSERT INTO tab2(col_1) VALUES(?)''', (k,))
    elif i.isdigit():
        i = int(i)
        if i % 2 == 0:
            cursor.execute('''INSERT INTO tab2(col_1) VALUES(?)''', (i,))
        else:
            b = "nechetnoe"
            cursor.execute('''INSERT INTO tab1(col_1) VALUES(?)''', (b,))

cursor.execute('''SELECT id FROM tab2''')
id_data = cursor.fetchall()
print(id_data)
len_id_data = len(id_data)
print(len_id_data)
if len_id_data > 5:
    cursor.execute('''DELETE FROM tab1 WHERE id = 1''')
    connect.commit()
else:
    cursor.execute('''UPDATE tab1 SET col_1="hello" WHERE id=1''')
    connect.commit()
