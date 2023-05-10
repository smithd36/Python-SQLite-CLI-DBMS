""" 
@Authors:
    - Drey Smith
    - Justus Contreas
    - German Ramirez

@Date: Spring Semester 2023

@Description:
    - This program serves as a fully operational CRUD interface for a Digital Display Company called ABC
    - The database will be called "ABC.sqlite"
    - The database will have 14 tables
    - The tables will be:
        - AdmWorkHours
        - Broadcasts
        - Model
        - Specializes
        - Administers
        - Client
        - Purchases
        - TechnicalSupport
        - Administrator
        - DigitalDIsplay
        - Salesman
        - Video
        - AirtimePackage
        - Locates
        - Site
    - The program will allow the user to:
        - Connect to databse after passing "Login_AUTH" which requires user to enter DB name
        - Display all tables in the database
        - Display all columns of a given table
        - Insert data into a table
        - Delete data from a table
        - Update data in a table

@Date: Spring Semester 2023

@Version: 1.0 

@Libraries:
    - sqlite3

This version of the program is to fulfill a project requirement for the Part 4 Project.

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
        print("\nserialNo SchedSys ModelNo")
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
        print("\nserialNo SiteCode")
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
           
def insert_element():
    """Function to insert a new element into the database"""
    table = input("Enter the name of the table to insert into: ")
    columns = []
    values = []
    # Get input for each column in the table
    for column in c.execute(f"PRAGMA table_info({table})"):
        columns.append(column[1])
        value = input(f"Enter {column[1]}: ")
        values.append(value)
    # Use INSERT INTO statement to add new element to the database
    c.execute(f"INSERT INTO {table} ({','.join(columns)}) VALUES ({','.join(['?']*len(values))})", values)
    conn.commit()
    print(f"New element added to {table} table.")

    #Display the column in the table user chosen to insert
    c.execute(f"SELECT * FROM {table}")
    for row in c.fetchall():
        print(f"{row[0]}\t{row[1]}")
                
def delete_element():
    table_name = input("Enter the name of the table to delete from: ")
    # Tuples containing the column name and type, like a dictionary
    column_aliases = {"VidCode": "videoCode", "VidLength": "videoLength", "modelNo": "ModelNo",
                      "screenSize": "ScreenSize", "siteCode": "siteCode", "type": "Type",
                      "schedulerSystem": "SchedulerSystem", "clientId": "ClientID", "packageId": "PackageID",
                      "empId": "EmpID", "day": "Day", "hours": "Hours", "serialNo": "SerialNo",
                      "commissionRate": "CommissionRate", "startDate": "StartDate", "lastDate": "LastDate",
                      "frequency": "Frequency", "name": "Name", "gender": "Gender", "address": "Address",
                      "phone": "Phone"} # Dictionary of column aliases

    # Get column name and value for searching
    search_strings = []
    # Loop until user enters 'done'
    while True:
        # Get column name and value for searching
        column_name = input("Enter the name of the column to search by (or 'done' if finished): ")
        if column_name == 'done': # Exit loop if user enters 'done'
            break
        column_alias = column_aliases.get(column_name, column_name) # Get column alias if it exists
        search_string = input(f"Enter a value for column '{column_name}': ") # Get search string
        search_strings.append((column_alias, search_string)) # Add column name and search string to list

    # Generate query and search strings
    query = f"DELETE FROM {table_name} WHERE " # Start query
    for column_name, search_string in search_strings: # Loop through search strings
        query += f"{column_name} LIKE ? AND " # Add search string to query
        # Add search string to list of search strings
    query = query[:-5]  # Remove trailing " AND " 

    # Confirm deletion with user
    print(f"You are about to delete the following record(s) from {table_name}:")
    c.execute(f"SELECT * FROM {table_name} WHERE {search_strings[0][0]} LIKE ?", ('%' + search_strings[0][1] + '%',)) # Execute query
    rows = c.fetchall() # Get rows
    for row in rows: # Print rows
        print(row) # Print row
    confirmation = input("Are you sure you want to proceed with the deletion? (y/n) ") # Confirm deletion
    if confirmation.lower() == 'y': # If user confirms deletion
        # Execute query
        c.execute(query, [('%' + search_string + '%') for _, search_string in search_strings]) #=
        conn.commit() # Commit changes
        print(f"{c.rowcount} record(s) deleted from {table_name}.") # Print number of rows deleted
    else:
        print("Deletion cancelled.") # Print message if user cancels deletion

def update_display():
    # Display all available digital displays
    print("Available digital displays:")
    c.execute("SELECT * FROM DigitalDisplay")
    displays = c.fetchall()
    for index, display in enumerate(displays):
        print(f"{index + 1}. {display}")
    
    # Prompt user to choose a display to update
    while True:
        try:
            choice = int(input("Enter the number of the display you want to update: "))
            if choice < 1 or choice > len(displays):
                raise ValueError()
            break
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and", len(displays))
    
    # Prompt user to enter new information for the display
    print("Current information for display", choice, ":")
    print(displays[choice - 1])
    new_info = input("Enter the new information for this display: ")
    
    # Update the display with the new information
    displays[choice - 1] = new_info
    
    # Display all digital displays with updated information
    print("Updated digital displays:")
    for index, display in enumerate(displays):
        print(f"{index + 1}. {display}")

def sign_out():
    """Function to sign out of the database"""
    print("You have successfully signed out of the database.")
    restart = input("Return to login? (y/n): ")
    if restart == "y":
        # Re-connect to the database
        login_auth = False
        while login_auth != True:
            LOGIN = input("LOGIN by entering DB name and file extension: ")
            if LOGIN == "ABC.sqlite" or LOGIN == "abc.sqlite" or LOGIN == "Abc.sqlite":
                print("Successfully connected to DB.\n")
                login_auth = True
            else:
                print("Invalid Entry. Please try again.")
                login_auth = False
    else:
        print("Thank you for using ABC Media Database. Goodbye!")
        conn.close()
        exit()

def search_display():
    """
    Function to search for a display in the database given a scheduler system
    """
    # Get scheduler system to search for
    scheduler_system = input("Enter the scheduler system to search for: ")
    
    # Search for displays with the given scheduler system
    c.execute("SELECT * FROM DigitalDisplay WHERE SchedulerSystem LIKE ?", ('%' + scheduler_system + '%',))
    displays = c.fetchall()

    # Display results
    print(f"Found {len(displays)} displays with scheduler system '{scheduler_system}':\n")
    for display in displays:
        print(display)

# Driver code
if __name__ == "__main__":
    """Main function to run the program"""
    print("Welcome to ABC Media Database\n")
    # Connect to the database
    login_auth = False
    while login_auth != True:
        LOGIN = input("LOGIN by entering DB name and file extension: ")
        if LOGIN == "ABC.sqlite" or LOGIN == "abc.sqlite" or LOGIN == "Abc.sqlite":
            print("Successfully connected to DB.\n")
            login_auth = True
        else:
            print("Invalid Entry. Please try again.")
            login_auth = False
        
    conn = sqlite3.connect(LOGIN)
    c = conn.cursor()
    # define dictionary with function names as keys
    menu_options = {
        "1": display_tables,
        "2": display_columns,
        "3": insert_element,
        "4": delete_element,
        "5": update_display,
        "6": search_display,
        "7": sign_out,
    }

    while True:
        # display menu
        choice = input("""
        1.) Display Tables 
        2.) Display Table Data
        3.) Insert Element
        4.) Delete Element
        5.) Update Display
        6.) Search Display
        7.) Exit

        Enter Choice: """)
        
        # check if choice is valid
        if choice in menu_options:
            # call function based on choice
            menu_options[choice]()
        else:
            print("Invalid choice. Please try again.")