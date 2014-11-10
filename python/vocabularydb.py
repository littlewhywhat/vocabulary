import MySQLdb

class Database:
    def open(self):
        HOST = '127.0.0.1'
        USER = 'root'
        PWD = 'vocabulary'
        DB = 'vocabulary'
        
        self.db = MySQLdb.connect(host=HOST, user=USER, passwd=PWD, db=DB)
        self.cur = self.db.cursor()

    def storySoFar(self) :
        cursor = self.cur
        cursor.execute('SELECT * FROM a ORDER BY id DESC LIMIT 5')
        for row in cursor.fetchall() :
           print row
        cursor.execute('SELECT * FROM words ORDER BY id DESC LIMIT 5')
        for row in cursor.fetchall() :
           print row
    def addGraph(self, wordgraph) :
        database = self.db
        cursor = self.cur
        try:
            for word, synonyms in wordgraph.items() :
                for synonym in synonyms :
                    cursor.callproc('insertAWW', (word, synonym, 0 , 0))
            database.commit()
        except:
            database.rollback()

    def close(self) :
        self.cur.close()
        self.db.close()