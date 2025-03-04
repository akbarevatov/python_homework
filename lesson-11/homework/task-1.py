import sqlite3

with sqlite3.connect("roster.db") as connection:
    
    # variable_number is a variable used for that question number
    cursor = connection.cursor()
    
    # 1
    query_1 = "Create Table If not exists Roster(Name text, Species text, Age int);"
    cursor.execute(query_1)
    
    # 2
    data_2 = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    query_2 = "Insert into Roster Values(?, ?, ?)"
    cursor.executemany(query_2, data_2)
    
    # 3
    query_3 = "Update Roster Set Name='Ezri Dax' Where Name='Jadzia Dax'"
    cursor.execute(query_3)

    # 4
    query_4 = "Select Name, Age From Roster Where Species='Bajoran'"
    result_4 = cursor.execute(query_4)
    print(result_4.fetchall())

    # 5
    query_5 = "Delete From Roster Where Age>100"
    cursor.execute(query_5)

    # 6 Bonus task
    cursor.execute("Alter Table Roster Add Column Rank text")
    data_6 = [
        ("Benjamin Sisko", "Captain"),
        ("Ezri Dax", "Lieutenant"),
        ("Kira Nerys", "Major")
    ]
    for data in data_6:
        query_6 = f"Update Roster Set Rank='{data[1]}' Where Name='{data[0]}'"
        cursor.execute(query_6)
    
    # 7
    query_7 = "Select * From Roster Order By Age Desc"
    result_7 = cursor.execute(query_7)
    print(result_7.fetchall())
