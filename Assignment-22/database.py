import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect("dolist.db")
        self.cursor = self.con.cursor()

    def get_tasks(self, id):
        if id == -1:
            query = "SELECT * FROM tasks ORDER BY is_done,Priority DESC"
            result = self.cursor.execute(query)
            tasks = result.fetchall()
        else:
            idd = id[1:]
            query = f"SELECT * FROM tasks WHERE id = {idd}"
            result = self.cursor.execute(query)
            tasks = result.fetchall()
        return tasks

    def add_new_task(self, new_title, new_description, time, priority):
        try:
            query = f"INSERT INTO tasks (title,desc,time,Priority) VALUES('{new_title}', '{new_description}','{time}', '{priority}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def task_done(self, id):
        ids = id[1:]
        query = f"SELECT * FROM tasks WHERE id = {ids}"
        result = self.cursor.execute(query)
        res = result.fetchall()
        if res[0][3] == 1:
            query = f"UPDATE tasks SET is_done = 0 WHERE id = {ids}"
        else:
            query = f"UPDATE tasks SET is_done = 1 WHERE id = {ids}"

        self.cursor.execute(query)
        self.con.commit()
        return True

    def task_delete(self, id):
        ids = id[1:]
        query = f"DELETE FROM tasks WHERE id = {ids}"
        result = self.cursor.execute(query)
        self.cursor.execute(query)
        self.con.commit()
        return True
