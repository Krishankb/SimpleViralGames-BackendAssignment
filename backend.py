import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("games.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,url TEXT, author TEXT, published_date TEXT)")
        self.conn.commit()

    def insert(self,name, url, author, published_date):
       
        self.cur.execute("INSERT INTO games VALUES (NULL,?,?,?,?)",(name, url, author, published_date))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM games")
        rows = self.cur.fetchall()
        return rows

    def search(self,name="",url="",author="",published_date=""):
        self.cur.execute("SELECT * FROM games WHERE name =? OR url=? OR author=? OR published_date=?",(name,url,author,published_date))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM games WHERE id = ?",(id,))
        self.conn.commit()

    def update(self,id,name, url, author, published_date):
        self.cur.execute("UPDATE games SET name =?, url=?, author=?, published_date=? WHERE id= ?",(name,url,author,published_date,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#connect()
#insert("The Oath of the Vayuputras","Amish Tripathi",2013,56817)
#delete(4)
#update(id=2,title="Scion of Ikshvaku",author="Amish Tripathi",year=2015,isbn=87541)
#print(view())
#print(search(year = 2011))