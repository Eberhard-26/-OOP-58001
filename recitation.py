import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\De Casa\Documents\\Database1.accdb;')
    print("Connected to a Database")

    Fullname = 'De Casa, Eberhard Josh'
    Laboratory = 95
    Assignment = 100
    Quiz = 95
    Exam = 98
    user_id = 11

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Fullname = ? WHERE id=?', (Fullname, user_id))
    record.execute('UPDATE Table1 SET Laboratory = ? WHERE id=?', (Laboratory, user_id))
    record.execute('UPDATE Table1 SET Assignment = ? WHERE id=?', (Assignment, user_id))
    record.execute('UPDATE Table1 SET Quiz = ? WHERE id=?', (Quiz, user_id))
    record.execute('UPDATE Table1 SET Exam = ? WHERE id=?', (Exam, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")
