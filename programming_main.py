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


#Register("Tristan ter Haar","+31620471504",1,"15-04-1998")
Stall(8470486)
conn.close()
