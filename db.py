
import sqlite3
import sys
import array





class Database():
    def __init__(self, db_file):
        self.connection=sqlite3.connect('testdatabase.db')
        self.cursor=self.connection.cursor()


    def add_user(self,user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
    def user_exists(self, user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id = (?)", (user_id,)).fetchall()
            return bool(len(result))
    def user_money(self, user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id = (?)", (user_id,)).fetchall()
            return int(result[0][2])  
    def set_money(self, user_id, money):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'money' = ? WHERE user_id=?",(money, user_id,))

    def add_check(self,user_id, money, bill_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'check' ('user_id', 'money','bill_id') VALUES (?,?,?)", (user_id,money, bill_id,))
    def get_check(self,bill_id):
       with self.connection:
            result=self.cursor.execute("SELECT * FROM 'check' WHERE bill_id =?", (bill_id,)).fetchall()
            if not bool(len(result)):
                return False
            return result[0]
    def delete_check(self,user_id, money, bill_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM 'check' WHERE 'bill_id'=?",(bill_id,))
    def state_subscribe(self,user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id=?",(user_id,)).fetchall()
            return result[0][3]
    def add_subscribe(self,user_id, subscribe):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'subscribe' = ? WHERE user_id=?",(subscribe, user_id,))
    def pay_subcribe(self, user_id, newmoney):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'money' = ? WHERE user_id=?",(newmoney, user_id,))

        












class get():
    def get_user():
        
            sqlite_connection = sqlite3.connect('testdatabase.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from users"""
            cursor.execute(sqlite_select_query)
            rows = cursor.fetchall()
            g=[0,]
            for row in rows:  
                g.append(row[1])
            return(g)
    


