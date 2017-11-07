import sqlite3, random, time
conn = sqlite3.connect("database.db")
c = conn.cursor()

def Register(name,tel,sex,bday):
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
    sql = "insert into users (name,tel,sex,bday,code) VALUES ('"+name+"','"+tel+"',"+str(sex)+",'"+bday+"',"+str(code)+")"
    c.execute(sql)
    print(code,"is de code voor",name)
    conn.commit()
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

def GetUserInfo(code,bday):
    try:
        int(code) #5459366 01-01-2000
    except:
        return
    if CheckAuth(code, bday):
        user_sql = "SELECT * FROM users WHERE code="+str(code)
        c.execute(user_sql)
        rows = c.fetchall()
        if len(rows) > 0:
            user = rows[0]
            return user

if CheckAuth(8470486, "15-04-1998"):
    print("Succesvol gecheckt")

#Register("Tristan ter Haar","+31620471504",1,"15-04-1998")
#Stall(8470486)
#BikePickup(8470486)
#conn.close()
