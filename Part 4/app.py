""" 
This version of the program is to fulfill a project requirement for the Part 4 Project.
This version of the program is considered to be in an Alpha state
and is not intended for final use.
Contributors:
    - Drey Smith
    - Justus Contreas
    - German Ramirez

At this time, the program establishes driver code for the first 2 functions,
display_tables() and display_columns(). The remaining functions are not yet
implemented.

Additional Notes:
    - The database file is named "ABC.sqlite"
    - Ensure that the database file is located in the same directory as this file
    - The database file is included in this repository

"""


import sqlite3

def display_tables():
    """Function to display all tables in the database"""
    # Display tables in the database
    print("Tables in", LOGIN , "are: ")
    #get tables from database
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #print tables
    for table in c.fetchall():
        print(table[0])

def display_columns():
    """Function to display columns of a given table
    including their specific column names. The names of the 
    tables in the DB will be: 
    AdmWorkHours, Broadcasts, Model, Specializes, Administers,
    Client, Purchases, TechnicalSupport, Administrator, DigitalDIsplay, Salesman,
    Video, AirtimePackage, Locates, Site"""

    table = input("Provide table name to display columns: ")
    if table == "AdmWorkHours":
        # Display columns of AdmWorkHours table
        c.execute("SELECT * FROM AdmWorkHours")
        # Print the column titles
        print("\nempID\tDate\t\tHours")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

    if table == "Broadcasts":
        c.execute("SELECT * FROM Broadcasts")
        # Print the column titles
        print("VideoCode SiteCode", end="")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")

    if table == "Model":
        c.execute("SELECT * FROM Model")
        # Print the column titles
        print("\nWidth\tHeight\tDepth\tScreenSize")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

    if table == "Specializes":
        c.execute("SELECT * FROM Specializes")
        # Print the column titles
        print("\nempID\tModelNo")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")

    if table == "Administers":
        c.execute("SELECT * FROM Administers")
        # Print the column titles
        print("\nempID\tSiteCode")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")

    if table == "Client":
        c.execute("SELECT * FROM Client")
        # Print the column titles
        print("\nClient#   Client Name")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")

    if table == "Purchases":
        c.execute("SELECT * FROM Purchases")
        # Print the column titles
        print("\nClient# empID PackageID CommRate")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")


    if table == "TechnicalSupport":
        c.execute("SELECT * FROM TechnicalSupport")
        # Print the column titles
        print("\nempID\tName")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


    if table == "Administrator":
        c.execute("SELECT * FROM Administrator")
        # Print the column titles
        print("\nempID\tName")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


    if table == "DigitalDisplay":
        c.execute("SELECT * FROM DigitalDisplay")
        # Print the column titles
        print("\nSerial# SchedSys ModelNo")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}")


    if table == "Salesman":
        c.execute("SELECT * FROM Salesman")
        # Print the column titles
        print("\nempID\tName")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


    if table == "Video":
        c.execute("SELECT * FROM Video")
        # Print the column titles
        print("\nVidCode VidLength")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


    if table == "AirtimePackage":
        c.execute("SELECT * FROM AirtimePackage")
        # Get the column names
        print("PkgID\tClass\tStart\tEnd\tFrequency\tVidCode")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")


    if table == "Locates":
        c.execute("SELECT * FROM Locates")
        # Print the column titles
        print("\nSerial# SiteCode")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


    if table == "Site":
        c.execute("SELECT * FROM Site")
        # Print the column titles
        print("\nSiteCode SiteType")
        print("~"*30)
        # Iterate over each row and print the values
        for row in c.fetchall():
            print(f"{row[0]}\t{row[1]}")


if __name__ == "__main__":
    """Main function to run the program"""
    print("Welcome to ABC Media Database\n")
    # Connect to the database
    login_auth = False
    while login_auth != True:
        LOGIN = input("LOGIN by entering DB name and file extension: ")
        if LOGIN == "ABC.sqlite":
            print("Successfully connected to DB.\n")
            login_auth = True
        else:
            print("Invalid Entry. Please try again.")
            login_auth = False
        
    conn = sqlite3.connect(LOGIN)
    c = conn.cursor()
    # decide function to execute based on user input
    while(1):
        choice = input("""
        1.) Display tables
        2.) Display columns within a Table
        3.) Insert a new table element
        4.) Delete a table element
        5.) Update a table element
        6.) Logout

        Enter Choice: """)
        if choice == "1":
            display_tables()
            continue
        if choice == "2":
            display_columns()
            continue
        # if choice == 3:
        # if choice == 4:
        # if choice == 5:
        # if choice == 6:
        # WILL BE FILLED UPDATED AS FUNCTIONS ARE DEVELOPED



    # Close the connection
    print("Disconnecting from: ", LOGIN, "\n")
    conn.close()