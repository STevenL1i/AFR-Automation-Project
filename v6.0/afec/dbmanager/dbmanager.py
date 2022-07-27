import traceback
import connectserver
import dbload as dbl

try:
    db = connectserver.connectserver("43.128.56.235", 3306, "StevenLi", "ABC@1120ab", "afec")
except Exception:
    db = connectserver.connectserver("43.128.56.235", 3306, "StevenLi", "ABC@1120ab")
cursor = db.cursor()

def dbcreate():
    dbname = input("please enter a database name: ")
    if dbname == "q" or dbname == "Q" or dbname == "quit" or dbname == "exit":
        return 0
    
    query = f'CREATE DATABASE {dbname};'
    cursor.execute(query)
    db.commit()


def dbinitialize():
    fd = open("dbcreate.sql", "r")
    query = fd.read()
    fd.close()
    query = query.split(";")

    for q in query:
        cursor.execute(q)
    db.commit()

    dbl.dbload_basic()


def dbload():
    dbl.dbload()


def dbclear():
    fd = open("dbclear.sql", "r")
    query = fd.read()
    fd.close()
    query = query.split(";")

    for q in query:
        cursor.execute(q)
    db.commit()

def dbdrop():
    fd = open("dbdrop.sql", "r")
    query = fd.read()
    fd.close()
    query = query.split(";")

    for q in query:
        cursor.execute(q)
    db.commit()



def main():
    while True:
        print("AFR Automation Table manager (AFEC version)")
        print()
        print("1.create database")
        print("2.load database")
        print("3.clear database")
        print("4.drop database")
        print()
        print("0.退出")
        choice = input("choose function： ")
        if choice == '1':
            try:
                dbinitialize()
            except Exception as e:
                print(traceback.format_exc())
                print(str(e))
            finally:
                input("press enter back to main menu")
        elif choice == '2':
            try:
                dbload()
            except Exception as e:
                print(str(e))
            finally:
                input("press enter back to main menu")
        elif choice == '3':
            try:
                dbclear()
            except Exception as e:
                print(str(e))
            finally:
                input("press enter back to main menu")
        elif choice == '4':
            try:
                dbdrop()
            except Exception as e:
                print(str(e))
            finally:
                input("press enter back to main menu")
        elif choice == '0':
            break
        

if __name__ == "__main__":
    main()