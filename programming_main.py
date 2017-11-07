import sqlite3, random, time
conn = sqlite3.connect("database.db")
c = conn.cursor()

def Register(name,tel,sex,bday):
    global c, conn
    code = random.randint(1000000,9999999)
    check_sql = "SELECT * FROM users WHERE code="+str(code)
    result = c.execute(check_sql)
    while result.rowcount > 0:
        code = random.randint(1000000,9999999)
        check_sql = "SELECT * FROM users WHERE code="+str(code)
        result = c.execute(check_sql)
    sql = "insert into users (name,tel,sex,bday,code) VALUES ('"+name+"','"+tel+"',"+str(sex)+",'"+bday+"',"+str(code)+")"
    c.execute(sql)
    print(code,"is de code voor",name)
    conn.commit()

def Stall(code):
    global c, conn
    timestamp = time.time()
    sql = "insert into storage (code,timestamp) VALUES ("+str(code)+","+str(round(timestamp))+")"
    c.execute(sql)
    print(code,"heeft een fiets gestald op",timestamp)
    conn.commit()

def BikePickup(code):
    global c, conn
    sql = "DELETE FROM storage WHERE code="+str(code)
    c.execute(sql)
    print(code,"heeft zijn fiets opgehaald.")
    conn.commit()

def LogAction(text):
    global c, conn
    sql = "INSERT INTO log (text) VALUES ("+text+")"
    c.execute(sql)
    conn.commit()

def CheckAuth(code, bday):
    global c, conn
    user_sql = "SELECT * FROM users WHERE code="+str(code)
    c.execute(user_sql)
    rows = c.fetchall()
    if len(rows) > 0:
        user = rows[0]
        if user[4] == bday:
            return True
    return False

def GetUserInfo(code,tel):
    if CheckAuth(code, tel):
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
