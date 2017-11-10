"""
This is the programming_main module.

This module has all the required backend functions, execept for the SendMessge function in the gmail_connector module.
"""

# Imports
import sqlite3, random, time
from gmail_connector import SendMessage

# Vars for the connection with the database
conn = sqlite3.connect("database.db")
c = conn.cursor()

def Register(name, tel, sex, bday, mail):
    """
    Registers the user in the database.

    Generates a random code between 1000000 and 9999999, checks if this number is already in the database and generates another one if it's already existing.
    Sends mail to the user with the unique code.
    """

    global c, conn
    code = random.randint(1000000,9999999)
    check_sql = "SELECT * FROM users WHERE code="+str(code)
    c.execute(check_sql)
    rows = c.fetchall()
    while len(rows) > 0:
        code = random.randint(1000000,9999999)
        check_sql = "SELECT * FROM users WHERE code="+str(code)
        c.execute(check_sql)
        rows = c.fetchall()
    sql = "insert into users (name,tel,sex,bday,code,mail) VALUES ('"+name+"','"+tel+"',"+str(sex)+",'"+bday+"',"+str(code)+",\""+mail+"\")"
    c.execute(sql)
    print(code,"is de code voor",name)
    conn.commit()
    SendMessage(mail,"Beste "+name+",\n\nU bent geregistreerd bij de NS fietsenstalling.\nUw unieke code is: "+ str(code)+". Bewaar deze goed.\n\nWe hopen u voldoende informatie te hebben verstrekt,\nHet NS team.")
    return code

def Stall(code):
    """
    Registers a bike as stored.
    """

    global c, conn
    timestamp = time.time()
    sql = "insert into storage (code,timestamp) VALUES ("+str(code)+","+str(round(timestamp))+")"
    returnval = 0
    try:
        c.execute(sql)
    except:
        returnval = -1
    print(code,"heeft een fiets gestald op",timestamp)
    conn.commit()
    return returnval

def BikePickup(code):
    """
    Registers a bike as picked up.
    """
    global c, conn

    check_sql = "SELECT * FROM storage WHERE code="+str(code)
    c.execute(check_sql)
    rows = c.fetchall()
    if len(rows) > 0:
        sql = "DELETE FROM storage WHERE code="+str(code)
        c.execute(sql)
        print(code,"heeft zijn fiets opgehaald.")
        conn.commit()
        return 0
    return -1

def LogAction(text):
    """
    Logging to the database.
    """
    global c, conn
    sql = "INSERT INTO log (text) VALUES (\""+text+"\")"
    print(sql)
    c.execute(sql)
    conn.commit()

def CheckAuth(code, bday):
    """
    2-factor authentication.
    Checks if the person with the unique code is actually the right person.
    Checked by checking in the database if the birthday is corrensponding with the unique code.
    """
    try:
        int(code)
    except:
        return False
    global c, conn
    user_sql = "SELECT * FROM users WHERE code="+str(code)
    c.execute(user_sql)
    rows = c.fetchall()
    if len(rows) > 0:
        user = rows[0]
        if user[4] == bday:
            return True
    return False

def GetInfo():
    """
    Get general information (system status, used and total amount bikestorages).
    """
    sql = "SELECT COUNT(*) as counter FROM storage"
    c.execute(sql)
    rows = c.fetchall()
    returndict = dict()
    if len(rows) > 0:
        counter = rows[0][0]
        returndict['counter'] = counter
        returndict['total_places'] = 666
        returndict['system_status'] = "OK"
    return returndict

def GetMailFromCode(code):
    """
    Gets the name and mail from the user from the database with the unique code.
    """
    sql = "SELECT mail, name FROM users WHERE code="+str(code)
    c.execute(sql)
    rows = c.fetchall()
    returndict = dict()
    if len(rows) > 0:
        mail = rows[0][0]
        name = rows[0][1]
        return [mail,name]
    return ""

def GetUserInfo(code,bday):
    """
    Gets the personal info from the database (Also using 2-factor authentication).
    """
    try:
        int(code) #5459366 01-01-2000
    except:
        return set()
    if CheckAuth(code, bday):
        user_sql = "SELECT * FROM users WHERE code="+str(code)
        c.execute(user_sql)
        rows = c.fetchall()
        if len(rows) > 0:
            user = rows[0]
            return user
        return set()
    return set()

if CheckAuth(8470486, "15-04-1998"):
    print("Succesvol gecheckt")

#Register("Tristan ter Haar","+31620471504",1,"15-04-1998")
#Stall(8470486)
#BikePickup(8470486)
#conn.close()
