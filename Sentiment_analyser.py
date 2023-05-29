from sqlite3 import Date
import tweepy # for accessing the twitter API
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime,timedelta, date
import mysql.connector as sqltor

#Establishment of connection with mysql database
mycon=sqltor.connect(host='localhost',user='root',password='cbytes',database='twitterdatabase')

#Checking if Connection is successful or not
if mycon.is_connected():
print("Successfully connected")
else:
print("Not connected")

#Using the cursor object and execute command to count all the tweets in the database
cursor=mycon.cursor()

#Deleting the tweets to accomodate new tweets
def Delete_the_tweets(Iterm,Leftover_tweets):

        #reading the data from text file 
        my_access_keys= open('File path to be entered here (text doc)','r').read().splitlines()

        #Authentication data
        my_API_key=my_access_keys[0]
        my_API_key_secret=my_access_keys[1]
        my_access_token=my_access_keys[2]
        my_access_token_secret=my_access_keys[3]

        #Twitter authentication handler code 
        auth= tweepy.OAuthHandler(consumer_key=my_API_key,consumer_secret=my_API_key_secret)
        auth.set_access_token(my_access_token,my_access_token_secret)
        api= tweepy.API(auth)

        Deletion_object="delete from tweets where Keyword='{}' Limit {}".format(Iterm,Leftover_tweets)
        cursor.execute(Deletion_object)
        return
      
def New_tweet_count(tweet_scanning_amt,str1):
#Checking if authentication of user is successful or not
#reading the data from text file
my_access_keys= open('File path to be entered here (text doc)','r').read().splitlines()

        #Authentication data
        my_API_key=my_access_keys[0]
        my_API_key_secret=my_access_keys[1]
        my_access_token=my_access_keys[2]
        my_access_token_secret=my_access_keys[3]

        #Twitter authentication handler code 
        auth= tweepy.OAuthHandler(consumer_key=my_API_key,consumer_secret=my_API_key_secret)
        auth.set_access_token(my_access_token,my_access_token_secret)
        api= tweepy.API(auth)

        #passing the parameters to cursor method 
        count=0
        tweets= tweepy.Cursor(api.search_tweets,q=str1,tweet_mode="extended",lang='en').items(tweet_scanning_amt)
        for tweet in tweets:
            count=count+1
        return count
      
def Sentiment_analysis(tweet_scanning_amt,str1,Iterm,Dateoftoday):
#reading the data from text file
my_access_keys= open('File path to be entered here (text doc)','r').read().splitlines()

        #Authentication data
        my_API_key=my_access_keys[0]
        my_API_key_secret=my_access_keys[1]
        my_access_token=my_access_keys[2]
        my_access_token_secret=my_access_keys[3]

        #Twitter authentication handler code 
        auth= tweepy.OAuthHandler(consumer_key=my_API_key,consumer_secret=my_API_key_secret)
        auth.set_access_token(my_access_token,my_access_token_secret)
        api= tweepy.API(auth)
       

        sid=SentimentIntensityAnalyzer()

        #passing the parameters to cursor method 
        tweets= tweepy.Cursor(api.search_tweets,q=str1,tweet_mode="extended",lang='en').items(tweet_scanning_amt)

        #Sentiment variables initialsed to zero
        positivesen=0
        negativesen=0
        neutralsen=0
        compoundsen=0
        weakpositive=0
        weaknegative=0
        count=0

        #Analysing the tweets 
        for tweet in tweets:
            final_text= tweet.full_text.replace('RT','').replace('"','')
            analysis = sid.polarity_scores(final_text)
            count=count+1
            compoundsen=analysis['compound']
            if compoundsen<=-0.5000 and compoundsen>=-1.0000:
                negativesen=negativesen+1
            if compoundsen>-0.5000 and compoundsen<0.0000:
                weaknegative=weaknegative+1
            if compoundsen==0.0000:
                neutralsen=neutralsen+1
            if (compoundsen>0.0000 and compoundsen<0.5000):
                weakpositive=weakpositive+1
            if compoundsen>=0.5000 and compoundsen<=1.000:
                positivesen=positivesen+1
            
            Insert_object ="""Insert into tweets values(\"{}\",'{}',{},{},{},{},{},'{}',{})""".format(final_text,Iterm,positivesen,negativesen,weaknegative,weakpositive,neutralsen,Dateoftoday,count)
            cursor.execute(Insert_object)
            mycon.commit()
       
        print_data="Select max(Positive),max(Negative),max(WeaklyPositive),max(WeaklyNegative),max(Neutral) from tweets where Keyword='{}'".format(Iterm)
        cursor.execute(print_data)
        data5=cursor.fetchall()
        return data5
      
def Sentiment_analytical(term):

#Using the cursor object and execute command to count all the tweets in the database  
base_empty_check="Select count(*) from tweets" 
cursor.execute(base_empty_check)
data=cursor.fetchall()


#Input the term to be searched 
stringinput=str(term)
Iterm=stringinput.lower()
str1=Iterm.split()
tweet_scanning_inputs=300

#Collect all the distinct keywords in the database or the previously searched terms 
term_check="Select distinct(Keyword) from tweets"
cursor.execute(term_check)
data1=cursor.fetchall()

#Getting the date at which tweet was scraped 
Dateoftoday=date.today()


#checking if the database is empty or not ...or... if the entered keyword is present in the database or not 
flag=0
if data[0][0]==0:
        flag=1
for i in data1:
    #print(Iterm,i[0],Iterm not in i[0])
    if (Iterm != i[0]):
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("Tweet getting scraped")
    Sentiment_analysis(tweet_scanning_inputs,str1,Iterm,Dateoftoday)
if flag==0:
#Iterm is present in table 
#Fetching the date from db for a specified keyword 
    date_check="Select distinct(date) from tweets where Keyword='{}'".format(Iterm)
    cursor.execute(date_check)
    data2=cursor.fetchall()
    print(data2)

    #this is used to add seven days to date at which tweet was scraped 
    date_after_7_days= data2[0][0] + timedelta(days = 7)
    print(date_after_7_days)
    

            
    #Date at which tweet was scrapped , check for a week time 
    if Dateoftoday>date_after_7_days: # if greater than 7 days then scrape new tweets
        
                
        # fetching the total number of old tweets from the db related to a specific topic 
        Old_tweet_count="Select count(*) from tweets where Keyword='{}'".format(Iterm)
        cursor.execute(Old_tweet_count)
        data3=cursor.fetchall()
        print(data3)

        #if User_entered_amount of new tweets are there regarding that specific topic only then so there analysis and put them in the database 
        if New_tweet_count(tweet_scanning_inputs,str1)>=data3[0][0]:

            #first delete the tweets of previous date otherwise more than 300 tweets will be there related to that specific Iterm in db
            Delete_the_tweets(Iterm,tweet_scanning_inputs)

            #Now save the new tweets in db 
            Sentiment_analysis(tweet_scanning_inputs,str1,Iterm,Dateoftoday)

        #if less than User_entered_amount of new tweets are there 
        else:
            Leftover_tweets=data3[0][0]-New_tweet_count(tweet_scanning_inputs,str1)

            #deleting the tweets equal to amount of left over tweets regarding to that specific topic 
            Delete_the_tweets(Iterm,Leftover_tweets)

            #Doing Sentiment analysis of left over tweets 
            Sentiment_analysis(Leftover_tweets,str1,Iterm,Dateoftoday)

    else:#just retrieve the tweets from the database regarding the specific topic 
        
        print_data="Select max(Positive),max(Negative),max(WeaklyPositive),max(WeaklyNegative),max(Neutral) from tweets where Keyword='{}'".format(Iterm)
        cursor.execute(print_data)
        data4=cursor.fetchall()
        return data4
