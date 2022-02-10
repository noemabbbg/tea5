
import sqlite3
import sys
import array

from dictant import SuicideBoy





class Databasee():
    def __init__(self, db_file):
        self.connection=sqlite3.connect('testdatabase1.db')
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
    def state_broadcast_boxer(self, user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id=?",(user_id,)).fetchall()
            return result[0][4]
    def add_user_broadcast_boxer(self,user_id, boxerbroadcast):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'boxerbroadcast' = ? WHERE user_id=?",(boxerbroadcast, user_id,))
    def state_broadcast_suicideboy(self, user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id=?",(user_id,)).fetchall()
            return result[0][5]
    def add_user_broadcast_suicideboy(self,user_id, suicideBoy):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'suicideboybroadcast' = ? WHERE user_id=?",(suicideBoy, user_id,))
    def state_broadcast_bastard(self, user_id):
        with self.connection:
            result=self.cursor.execute("SELECT * FROM 'users' WHERE user_id=?",(user_id,)).fetchall()
            return result[0][6]
    def add_user_broadcast_bastard(self,user_id, bastard):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'bastardbroadcast' = ? WHERE user_id=?",(bastard, user_id,))












class get():  # сделаю буфферную k которая будет овтечать за то, какой столбец я беру - с айди или тех кто на что подписан  
    def get_user(k):
        
            sqlite_connection = sqlite3.connect('testdatabase1.db')
            cursor = sqlite_connection.cursor()

            sqlite_select_query = """SELECT * from users"""
            cursor.execute(sqlite_select_query)
            rows = cursor.fetchall()
            g=[0,]
            for row in rows:  
                g.append(row[k])
            return(g)
    
    


