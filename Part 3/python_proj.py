import sqlite3
import sys

# define a function to get the distinct salesmen names and counts
def distinct_salesmen():
    """List the distinct names of all salesmen and the number of salesmen with that name.
    The output should be in the ascending order of the salesmen name. If multiple salesmen have the
    same name, show all attribute values for those salesmen."""
    # connect to the ABC.sqlite database
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()
# execute a SQL statement to get the distinct salesmen names and counts
    c.execute('''SELECT SUBSTR(name, 1, INSTR(name || ' ', ' ') - 1) AS first_name, COUNT(*) as cnt 
                 FROM Salesman 
                 GROUP BY first_name 
                 ORDER BY first_name ASC''')
    # fetch all the results into a list of tuples
    results = c.fetchall()

    print("Name cnt")
    print("------------------")
    # loop through the results and print each row
    for result in results:
        # if the count is 1, print the name and count
        if result[1] == 1:
            print(result[0] + " " + str(result[1]))
        # if the count is greater than 1, print the name and count and the duplicate names
        else:
            # execute a SQL statement to get the duplicate names
            c.execute('''SELECT * FROM Salesman WHERE SUBSTR(name, 1, INSTR(name || ' ', ' ') - 1) = ?''', (result[0],))
            # fetch all the results into a list of tuples
            duplicates = c.fetchall()
            print(result[0] + " " + str(result[1]), end="")
            # loop through the duplicate names and print them
            for i, d in enumerate(duplicates):
                # if this is the first duplicate name, print the name and count
                print(" (" + str(d[0]) + "," + d[1] + "," + d[2] + ")", end="")
            print()

    conn.close()

# define a function to get the names of technical supports that specialize in a given model
def tech_supports_by_model(model_no):
    """Find the technical supports that specialize a specidied model. Display the names of
    those technical supports. The specified model no should be a parameter input through the main
    program."""
    # connect to the ABC.sqlite database
    conn = sqlite3.connect('ABC.sqlite')
    # create a cursor object to execute SQL statements
    c = conn.cursor()

    # execute a SQL statement to get the names of technical supports that specialize in the given model
    c.execute('''SELECT name FROM TechnicalSupport WHERE empId IN (SELECT empId FROM Specializes WHERE modelNo = ?)''', (model_no,))
    # fetch all the results into a list of tuples
    results = c.fetchall()

    # print the column headers
    print("Name")
    print("------------------")
    # loop through the results and print each row
    for result in results:
        print(result[0])

    # close the database connection
    conn.close()

# define a function to get the count of administrators, salesmen, and technical supports
def count_roles():
    """Calculate number of administrators, salesmen, and technical supports. Display the
    results in the follownig format."""
    # connect to the ABC.sqlite database
    conn = sqlite3.connect('ABC.sqlite')
    # create a cursor object to execute SQL statements
    c = conn.cursor()

    # execute a SQL statement to get the count of administrators, salesmen, and technical supports
    c.execute('''SELECT "Administrator" as Role, COUNT(*) as cnt FROM Administrator
                 UNION
                 SELECT "Salesmen" as Role, COUNT(*) as cnt FROM Salesman
                 UNION
                 SELECT "Technicians" as Role, COUNT(*) as cnt FROM TechnicalSupport''')
    # fetch all the results into a list of tuples
    results = c.fetchall()

    # print the column headers
    print("Role cnt")
    print("------------------")
    # loop through the results and print each row
    for result in results:
        print(result[0] + " " + str(result[1]))

    # close the database connection
    conn.close()

def query2(param_schedular_system):
    '''
    Find the digital displays with a given scheduler system. Show their serial numbers,
    model numbers, and the names of technical supports who specialize their models. The scheduler
    should be a parameter input through the main program.
    To get the answer to this question, the command to run is
    python proj.py 2 <param_schedular_system>
    '''    
    # connect to project database
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()

    # query db for displays with given scheduler system
    c.execute('''
        SELECT DigitalDisplay.serialNo, DigitalDisplay.modelNo, TechnicalSupport.name
        FROM DigitalDisplay
        JOIN Specializes ON DigitalDisplay.modelNo = Specializes.modelNo
        JOIN TechnicalSupport ON Specializes.empId = TechnicalSupport.empId
        WHERE DigitalDisplay.schedulerSystem = ?
    ''', (param_schedular_system,))

    # print displays with specified scheduler system
    print('Digital displays with scheduler system', param_schedular_system, ':')
    for row in c.fetchall():
        print(row)

    # close connection
    conn.close()


def query5():
    """
    Find the total working hours of each administrator. 
    Display the administrators employee ID, name, and total working hours
    in ascending order of the total working hours. To get the answer to this
    question, the command to run is python proj.py 5
    """
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()

    #query db for total working hours for each administrator
    c.execute('''
        SELECT Administrator.empId, Administrator.name, SUM(AdmWorkHours.hours)
        FROM Administrator
        LEFT JOIN AdmWorkHours ON Administrator.empId = AdmWorkHours.empId
        GROUP BY Administrator.empId
        ORDER BY SUM(AdmWorkHours.hours) ASC
    ''')

    #print total working hours
    print('Total working hours for each administrator:')
    for row in c.fetchall():
        print(row)

    #close connection
    conn.close()

def query7():
    """
    Order the salesmen with descending order of their average
    commission rates. Display each salesman's name and the average 
    commission rate. To get the answer to this question, the command to run is
    python proj.py 7
    """
    # connect to the project database
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()

    # execute Query 7 from ABC.sqlite
    c.execute("SELECT Salesman.name, AVG(Purchases.commissionRate) as avg_rate FROM Salesman JOIN Purchases ON Salesman.empId = Purchases.empId GROUP BY Salesman.empId ORDER BY avg_rate DESC")
    
    # print salesman name and average commission rate
    rows = c.fetchall()
    print("Salesman\tAverage Commission Rate")
    for row in rows:
        print(row[0] + "\t" + str(row[1]))

    # close connection
    conn.close()

def query1(param_street_name):
    '''Find the sites that are on a given street (i.e., the address 
    contains the street name (case insensitive)). Show the detailed 
    information of each site. To get the answer to this question, the 
    command to run is python proj.py 1'''

    # connect to project database
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()

    # query db for sites on the given street
    c.execute('''
        SELECT *
        FROM Site
        WHERE lower(address) LIKE ?
    ''', ('%' + param_street_name.lower() + '%',))

    # print site information such as address, phone number, people on site, and the name of the client
    print('Site Information:')
    for row in c.fetchall():
        print(row)

    # close connection
    conn.close()


def query4(param_phone_no):
    '''Find the clients with a given phone no. The phone number should 
    be a parameter input through the main program. To get the answer of 
    this question, the command to run is python proj.py 4'''

    # connect to project database
    conn = sqlite3.connect('ABC.sqlite')
    c = conn.cursor()

    # query db for clients with given phone number using parameterized query
    c.execute('''
        SELECT *
        FROM Client
        WHERE phone = ?
    ''', (param_phone_no,))

    #print client information
    print('Client Information:')
    for row in c.fetchall():
        print(row)

    #close connection
    conn.close()


# check if this file is being run as the main program
# check the command-line arguments and call the appropriate function
if sys.argv[1] == '1':
    query1(sys.argv[2])
elif sys.argv[1] == '2':
    query2(sys.argv[2])
elif sys.argv[1] == '3':
    distinct_salesmen()
elif sys.argv[1] == '4':
    query4(sys.argv[2])
elif sys.argv[1] == '5':
    query5()
elif sys.argv[1] == '6':
    tech_supports_by_model(sys.argv[2])
elif sys.argv[1] == '7':
    query7()
elif sys.argv[1] == '8':
    count_roles()
else:
    print('Invalid query number')