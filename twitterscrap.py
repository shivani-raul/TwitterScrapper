import sys
import json
import requests
from requests_oauthlib import OAuth1
class Twisc:
    def __init__(self,apikey,secretkey,accesstoken,accesssecret):
        self.apikey=apikey
        self.secretkey=secretkey
        self.accesstoken=accesstoken
        self.accesssecret=accesssecret

    def get_user_id(self,username):
        usernames = "usernames={}".format(username)
        user_fields = "user.fields"
        url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
        #"https://api.twitter.com/labs/2/users/by?usernames=twitterdev&user.fields=created_at,description,pinned_tweet_id"
        json_response = self.endcon(url)
        return json.loads(json.dumps(json_response,sort_keys=True))['data'][0]['id']
    
    def create_url(self,username,tweet_fields = 'created_at',expansions = 'author_id',user_fields = '',max_tweet=10):
        self.username = username
        self.tweet_fields = tweet_fields
        self.expansions = expansions
        self.user_fields = user_fields
        self.max_tweet = max_tweet
        user_id = self.get_user_id(username)
        tweet_field = "tweet.fields={}".format(tweet_fields)
        expansion = "expansions={}".format(expansions)
        user_field = "user.fields={}".format(user_fields)       
        return "https://api.twitter.com/2/users/{}/tweets?{}&{}&{}&max_results={}".format(user_id,tweet_field,expansion,user_field,max_tweet)

    def endcon(self,url):
        self.url=url
        response = requests.request("GET", url, auth=OAuth1(self.apikey,self.secretkey,self.accesstoken,self.accesssecret))
        #print(response.json())
        return response.json()

    def get_tweet_info(self):  
        tweet_url = self.create_url(self.username,self.tweet_fields,self.expansions,self.user_fields,self.max_tweet)
        json_response = self.endcon(tweet_url)
        #print(json_response)
        p=json.loads(json.dumps(json_response, sort_keys=True))
        return p
    
    def getdata(self,tweet_info):
        self.tweet_info=tweet_info
        tweet_info_json = self.get_tweet_info()
        for i in range(len(tweet_info_json['data'])):
            for x in tweet_info_json['data'][i].keys():
                if x == "author_id":
                    tweet_info.append([tweet_info_json['data'][i][x]])
                elif x == "public_metrics":
                    tweet_info[i+1].append(tweet_info_json['data'][i][x]['like_count'])
                    tweet_info[i+1].append(tweet_info_json['data'][i][x]['retweet_count'])
                else:
                    tweet_info[i+1].append(tweet_info_json['data'][i][x])

        

        