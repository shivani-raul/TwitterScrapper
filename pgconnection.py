import logging
import psycopg2

class dbpostgre:
    def __init__(self,host,port,database,user,password):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password
        self.con = psycopg2.connect(
            host = "localhost",
            port="5432",
            database="db1",
            user="postgres",
            password="shivani")
        logging.warning("Connecting to DB")
        #print("Connecting to DB.....")
    
    def createcursor(self):
        self.cur=self.con.cursor()
        return self.cur
        
    def createtable(self,tablename):
        query="""CREATE TABLE IF NOT EXISTS {}(AuthorID varchar(500),Createdtime varchar(100),TweetID varchar(100),Likes varchar(100),Retweets varchar(100),Description varchar(500));""".format(tablename)
        self.cur.execute(query)
        return self.cur

    def gettable(self,tablename):
        self.tablename=tablename

    def insertdata(self,tablename,rec):
        for i in rec:
            self.cur.execute("""INSERT INTO {} VALUES {}""".format(tablename,tuple(i)))

    def closecon(self):
        self.con.commit()
        self.cur.close()
        self.con.close()


        
        

