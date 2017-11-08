import sqlite3, random, time

from gmail_connector import SendMessage

conn = sqlite3.connect("database.db")
c = conn.cursor()

def Register(name,tel,sex,bday,mail):
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
    global c, conn
    sql = "INSERT INTO log (text) VALUES (\""+text+"\")"
    print(sql)
    c.execute(sql)
    conn.commit()

def CheckAuth(code, bday):
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


def GetUserInfo(code,bday):
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
