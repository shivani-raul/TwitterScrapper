import twitterscrap
import re
import logging
import pgconnection
import mysqlcon
import csvparsing
from pdf_file import PDF
tweet=twitterscrap.Twisc('apik','api-secret','access-k','access-secret')
tweet.create_url('ManUtd','created_at,public_metrics','author_id','',10)
tweet_info = [['AuthorID','Createdtime','TweetID','Likes','Retweets','Description']]
tweet.getdata(tweet_info)
def clean(text):
    text=re.sub(r'[^A-Za-z0-9/:.]+', ' ', text)
    text=re.sub('\\n','',text)             #removes \n string
    text=re.sub('https?:\/\/\S+','',text) #removes the http link after text
    return text
for i in range(1,len(tweet_info)):
  tweet_info[i][5] = clean(tweet_info[i][5])
#print(tweet_info)
#postgres
parser=csvparsing.parsing('twitter.csv',tweet_info[0],tweet_info[1:])
obj=pgconnection.dbpostgre("localhost","5432","db1","postgres","shivani")
cur=obj.createcursor()
cur=obj.createtable('twitter')
obj.gettable('twitter')
obj.insertdata('twitter',tweet_info[1:])
pdf=PDF("P","mm","letter")
header=parser.header
value=parser.value
pdf.add_page()
pdf.alias_nb_pages()
pdf.maketable(header,value)
logging.info("DATA in PDF with PG")
pdf.output("twitter.pdf")
obj.closecon()
#sql
parser2=csvparsing.parsing('twitter.csv',tweet_info[0],tweet_info[1:])
obj2=mysqlcon.dbmysql(host ="localhost",database="dbsql",user="root",password="shiv@ni123")
cur=obj2.createcursor()
cur=obj2.createtable('twitter')
obj2.gettable('twitter')
obj2.insertdata('twitter',tweet_info[1:])
pdf2=PDF("P","mm","letter")
header=parser.header
value=parser.value
pdf2.add_page()
pdf2.alias_nb_pages()
pdf2.maketable(header,value)
logging.info("DATA in PDF with SQL")
pdf2.output("twitter.pdf")
obj2.closecon()




'''from os import access
from requests import auth
import tweepy
from tweepy import OAuthHandler
import json
import datetime
access_token='--add-your-key--'
access_token_secret='--add-your-key--'
consumer_key='--add-your-key--'
consumer_secret='--add-your-key--'
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
print("Authenticated")
api=tweepy.API(auth,wait_on_rate_limit=True)'''