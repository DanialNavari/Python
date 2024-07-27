import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("alarm.db")
        self.cursor = self.con.cursor()

    def get_alarm(self):
        query = "SELECT * FROM alarm WHERE 1"
        result = self.cursor.execute(query)
        alarm_selected = result.fetchall()
        return alarm_selected
            
    def add_alarm(self, alarm_message, alarm_hour, alarm_minute):
        try:
            query = f"INSERT INTO alarm(message,hour,minute) VALUES('{alarm_message}',{alarm_hour},{alarm_minute})"
            self.cursor.execute(query)
            self.con.commit()   
            return True
        except:
            return False
        
    def edit_alarm(self, id):
        ...
        
    def del_alarm(self, id):
        idd = id[1:]
        query = f"DELETE alarm WHERE id = {idd}"
        self.cursor.execute(query)
        self.con.commit()
        return True
    
    
        