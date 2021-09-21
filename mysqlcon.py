import mysql.connector
import logging
import pymysql

class dbmysql:
    def __init__(self,host,database,user,password):
        self.host=host
        self.datbase=database
        self.user=user
        self.password=password
        self.con = pymysql.connect(
            host = "localhost",
            database="dbsql",
            user="root",
            password="shiv@ni123")
        logging.warning("Connecting to MYSQLDB")
    
    def createcursor(self):
        self.cur=self.con.cursor()
        return self.cur
        
    def createtable(self,tablename):
        query="""CREATE TABLE IF NOT EXISTS {}(AuthorID varchar(500),Createdtime varchar(100),TweetID varchar(100),Likes varchar(100),Retweets varchar(100),Description varchar(500));""".format(tablename)
        self.cur.execute(query)
        return self.cur
        
    def gettable(self,tablename):
        self.tablename=tablename
        return tablename

    def insertdata(self,tablename,rec):
        for i in rec:
            self.cur.execute("""INSERT INTO {} VALUES {}""".format(tablename,tuple(i)))

    def closecon(self):
        self.con.commit()
        self.cur.close()
        self.con.close()

        
