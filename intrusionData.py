import sqlite3
import time

class textStorage:
    def __init__(self, dbName):
        self.conn = sqlite3.connect(dbName)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS texts
        (id INTEGER PRIMARY KEY,
         time TEXT,
         text TEXT)
        ''')
        self.conn.commit()

    def add_text(self, timeInfo, text):
        self.cursor.execute("INSERT INTO texts (time, text) VALUES (?, ?)", (timeInfo, text))
        self.conn.commit()

    def get_text(self, timeInfo):
        self.cursor.execute("SELECT text FROM texts WHERE time = ?", (timeInfo, ))
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            return "No intrusion data found !!"



# text_storage = textStorage("text.db")
#
# text_storage.add_text("2024-04-26 10:00", "test text1")
# text_storage.add_text("2024-04-26 10:00", "test text2")
# text_storage.add_text("2024-04-26 10:00", "test text3")
# text_storage.add_text("2024-04-28 10:00", "test text1")
# text_storage.add_text("2024-04-26 16:00", "test text3")
#
# print(text_storage.get_text("2024-04-26 10:00"))
#
# now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# print(now)

