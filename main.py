'''Employee_information_system which works on the
adding record,
updating record,
deleting record and
selecting record........'''
from mysql.connector import connect
conn= connect(
    host="localhost",
    user="root",
    password="Password",
    database="Employee_information_system"
)
curr=conn.cursor()
def add():
    curr= conn.cursor()
    sql = "insert into employee values(%s, %s, %s, %s, %s)"
    list = []
    while True:
        eid = int(input("Enter employee id : "))
        ename = input("Enter employee name : ")
        esal = int(input("Enter employee esal : "))
        emob = int(input("Enter employee mobile no :  "))
        eadd = input("Enter employee add : ")
        val = (eid, ename, esal, emob, eadd)
        list.append(val)
        ch1= input("Enter your choice for adding more record in a table chose 'y' for continue otherwise 'n' : ")
        if ch1 == 'n':
            print("User does not want to add more element!!\n")
            break
    curr.executemany(sql, list)
    conn.commit()
    print(curr.rowcount,"Row added..........\n\n")


def update():
    curr = conn.cursor()
    print("1. for updating ename\r")
    print("2. for updating esal\r")
    print("3. for updating emob\r")
    print("4. for updating eadd\r")
    print("5. for updating all\r")
    choice = int(input("Enter your choice for updating table :"))
    if choice==1:
        while True:
            sql = "update employee set ename= %s where eid= %s"
            list = []
            eid = int(input("Enter employee id : "))
            ename = input("Enter employee name : ")
            val = (ename,eid)
            list.append(val)
            ch1 = input("Enter your choice for updating more record in a table chose 'y' for continue otherwise 'n' : ")
            if ch1 == 'n':
                print("User does not want to update more element!!\n")
                break
        curr.executemany(sql, list)
        conn.commit()
    print(curr.rowcount,"Row updated.........\n\n")
    if choice==2:
        while True:
            sql = "update employee set esal= %s where eid= %s"
            list = []
            eid = int(input("Enter employee id : "))
            esal = input("Enter employee salary : ")
            val = (esal,eid)
            list.append(val)
            ch1 = input("Enter your choice for updating more record in a table chose 'y' for continue otherwise 'n' : ")
            if ch1 == 'n':
                print("User does not want to update more element!!\n")
                break
        curr.executemany(sql, list)
        conn.commit()
        print(curr.rowcount,"Row updated.........\n\n")
    if choice==3:
        while True:
            sql = "update employee set emob= %s where eid= %s"
            list = []
            eid = int(input("Enter employee id : "))
            emob = input("Enter employee mobile no : ")
            val = (emob,eid)
            list.append(val)
            ch1 = input("Enter your choice for updating more record in a table chose 'y' for continue otherwise 'n' : ")
            if ch1 == 'n':
                print("User does not want to update more element!!\n")
                break
        curr.executemany(sql, list)
        conn.commit()
        print(curr.rowcount,"Row updated.........\n\n")
    if choice==4:
        while True:
            sql = "update employee set eadd= %s where eid= %s"
            list = []
            eid = int(input("Enter employee id : "))
            eadd = input("Enter employee address : ")
            val = (eadd,eid)
            list.append(val)
            ch1 = input("Enter your choice for updating more record in a table chose 'y' for continue otherwise 'n' : ")
            if ch1 == 'n':
                print("User does not want to update more element!!\n")
                break
        curr.executemany(sql, list)
        conn.commit()
        print(curr.rowcount,"Row updated.........\n\n")
    if choice==5:
        while True:
            sql = "update employee set ename= %s ,esal=%s,emob=%s,eadd=%s where eid= %s"
            list = []
            eid = int(input("Enter employee id : "))
            ename = input("Enter employee name : ")
            esal = input("Enter employee salary : ")
            emob = input("Enter employee mobile no : ")
            eadd = input("Enter employee address : ")

            val = val = (eid,ename,esal,emob,eadd )
            list.append(val)
            ch1 = input("Enter your choice for updating more record in a table chose 'y' for continue otherwise 'n' : ")
            if ch1 == 'n':
                print("User does not want to update more element!!\n")
                break
        curr.executemany(sql, list)
        conn.commit()
        print(curr.rowcount,"Row updated.........\n\n")



def delete():
    curr = conn.cursor()
    print("1. for deleting single row")
    print("2. for deleting all record of table")
    choice = int(input("Enter choice for deleting record: "))

    if choice == 1:
        sql = "DELETE FROM employee WHERE eid=%s"
        values = []      # correct placement + correct name

        while True:
            eid = int(input("Enter employee id : "))
            values.append((eid,))

            ch1 = input("Enter your choice for deleting more record in a table chose 'y' for continue otherwise 'n' :")
            if ch1.lower() == 'n':
                print("User does not want to delete more Record!!\n")
                break

        curr.executemany(sql, values)
        conn.commit()

    elif choice == 2:
        sql = "DELETE FROM employee"
        curr.execute(sql)
        conn.commit()

    print(curr.rowcount, "Row deleted.........\n\n")


def select_specific():
    print("1. for selecting on the basis of salary\r")
    print("2.  for selecting on the basis of id\r")
    choice = int(input("Enter your choice:"))
    curr = conn.cursor()
    if choice==1:
        sql = "select * from employee where esal>%s"
        list = []
        esal = int(input("Enter employee esal : "))
        val=(esal,)
        curr.execute(sql, val)
        print("========================================")
        print("||eid||||ename||||esal||||emob||||eadd||")
        print("========================================")
        for record in curr:
            print(record)
        print(curr.rowcount,"Specific record selected.........\n\n")
    elif choice==2:
        sql = "select * from employee where eid=%s"
        list = []
        eid = int(input("Enter employee eid : "))
        val=(eid,)
        curr.execute(sql, val)
        print("==================================================")
        print("eid      ename       esal        emob        eadd")
        print("==================================================")
        for x in curr:
            print(x[0], "\t", x[1], "\t\t", x[2], "\t", x[3], "\t", x[4])
        print(curr.rowcount,"row record selected.........\n\n")


def select_all():
    print("==================================================")
    print("eid      ename       esal        emob        eadd")
    print("==================================================")
    curr = conn.cursor()
    sql = "select * from employee"
    curr.execute(sql)
    for x in curr:
        print(x[0],"\t\t", x[1],"\t\t", x[2],"\t\t", x[3],"\t\t",x[4])

    print( curr.rowcount,"row record selected.........\n\n")



#sql= "create table employee(eid int,ename varchar(20),esal int ,emob int ,eadd varchar(30))"
#curr.execute(sql)

print("==============================================================")
print("                  Employee information system                 ")
print("==============================================================")

while True:
    print("All operation details ......................\n")
    print("1. for add record in a table\r")
    print("2. for update record in a table\r")
    print("3. for delete record in a table\r")
    print("4. for select some specific record from a table\r")
    print("5. for select all record from a table\r")
    print("6. for exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add()
    elif ch==2:
        update()
    elif ch==3:
        delete()
    elif ch==4:
        select_specific()
    elif ch == 5:
        select_all()
    elif ch == 6:
        exit()
    else:
        print("Default choice !!!!!!!!!!\n ")
        choice=input("If u want to continue then press 'y' otherwise press 'n':")
        if choice == 'n':
            print("user does not want to continue........")

conn.close()
curr.close()



