This file contains the explanation of the code for the analysis of the tweets scraped using twitter API and storing it in the database(using MYSQL connector) and displaying the results.

        #reading the data from text file 
        my_access_keys= open('read the keys by entering the path here of the text doc ','r').read().splitlines()

        #Authentication data
        my_API_key=my_access_keys[0]
        my_API_key_secret=my_access_keys[1]
        my_access_token=my_access_keys[2]
        my_access_token_secret=my_access_keys[3]

        #Twitter authentication handler code 
        auth= tweepy.OAuthHandler(consumer_key=my_API_key,consumer_secret=my_API_key_secret)
        auth.set_access_token(my_access_token,my_access_token_secret)
        api= tweepy.API(auth)
Here the access keys are stored in another text file which are accessed using the file read operation. In the file pointer value of every key is being saved as list and then every key is being allotted its value. After that using the tweepy authentication handler , all four keys are passed as parameters to the functions which basically verifies the authenticity of the user.

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
The above code that initially each tweet is scraped using twitter API and then all those scraped Tweets are stored in tweet which is basically the variable which contains the all the scraped tweets. Each tweet undergoes required pre- processing .i.e. if a tweet has a heading as RT then to clear it , replace function has been used which replaces the heading "RT" with white spaces. The importance of doing this is that , now every tweet which has the starting as "RT" will be blank thereafter and hence one word less for analysis. Similarly, all the double quotes are also replaced from tweet. Further now sentiment intensity analyser has been used which is basically the object of vader lexicon for calculating the sentiment of tweet and hence this tweet is passed as a parameter to the polarity_scores method which basically returns the sentiment in a dictionary form: { 'pos' : 0.6575 , 'neg' : -0.6363 , "neu" : 0.6273 , "compound" : 0.7373 }. We will be utilizing the ‘compound’ element of the dictionary to classify our tweet into the respective categories.Each category has its individual counter and every time the respective counters are increased by one , whenever the compound score falls in one of the categories. Now this data of incremented counter with the respective tweet is added to the database, along with the tweet. For this I have used the sql connector for storing the data of the tweets in the database.

         def Delete_the_tweets(Iterm,Leftover_tweets):

        #reading the data from text file 
        my_access_keys= open('Path of the user authentication keys doc','r').read().splitlines()

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
The above code shows the deletion of tweets, first the authentication takes place and then the tweets get deleted. Here deletion of tweets have been made because when the same keyword was searched again after the time period of seven days , then if it happens that regarding that same keyword 300 latest new tweets are not found , then to maintain the number of tweets in the database as 300 only , remaining number of tweets are deleted from the database and now all the new tweets found will be stored in the database with the remaining one’s giving the total count as 300.

       def New_tweet_count(tweet_scanning_amt,str1):
        #Checking if authentication of user is successful or not 
        #reading the data from text file 
        my_access_keys= open('path of user authentication keys','r').read().splitlines()

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
The above code shows the new tweet count function where first the authentication of user takes place and then we search and count for the new tweets to check whether there are 300 new tweets or not. For searching, tweepy library’s cursor method is used which has parameter as api.search_tweet which searches for tweets on twitter , second parameter is the keyword regarding which search has to be made , third parameter is the tweet_mode which is set as extended which means full text tweet will be scraped and nothing will be truncated and all those tweets having language as English. The items parameter sets the limit for the number of tweets to be scraped or analysed. The results are stored in tweets variable and then iterations are made, with the increment of counter at each step.

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
In the above code , first we count the tweets in the whole database. Then we change the format of our term by making it to lower case and splitting it to many parts (if the search term contains many words). Then we pass a query to MySql for selecting all the distinct keywords and storing it in a object. Then we put a check regarding the fact that the database is originally is empty or not or the database contains the searched term or not. If the term is originally not present in the database then the tweets related to that term will be scraped from twitter using twitter API and stored in the database and the results are displayed to the user in the form of the positive , negative and neutral tweets. If the searched term is already there in the database , then a further check is put on the term that if the term was searched in the database more than 7 days ago then scrape new tweets but if the new tweets on twitter are not equal to 300 (default amount) then scrape all those tweets from twitter and delete only the leftover tweets(original tweets minus the new tweets) from database which could maintain the total tweet count in the database as 300. If the searched term is not older than 7 days then the analytical results are displayed directly.
