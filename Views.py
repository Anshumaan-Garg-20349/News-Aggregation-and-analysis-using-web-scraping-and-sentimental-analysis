from django.http import HttpResponse, HttpResponseRedirect
        from django.shortcuts import HttpResponse,render
        from .Sentiment_analyser import Sentiment_analytical
        from .My_tweet_analysis import *
        from .main import Scrapper
        from django.urls import reverse
        from django.http import Http404, HttpResponse
        import datetime
        from .models import News
        import time
        import mysql.connector as sqltor
        
        
        
        def index(request):
            return render(request,'index.html')
        
        def mynews(request):
           return render(request,'MyNews.html')
           return HttpResponse("This is analysis page")
           return render(request,'MyNews.html')
        
        
        
        def Scrape(request):
            #checkig if the function is of type POST
            if request.method=='POST':
                #getting the entered term and getting the required with it from Googlenews 
                Keyterm=request.POST.get('Keyterm')
                #print(Keyterm)
                resultset=Scrapper(Keyterm)
                print(resultset)
                context = {
                "result":resultset
            }
                return render(request,'index.html', context
                )
        def Trialfunc(InputTerm):
            #Establishment of connection with mysql database
            mycon=sqltor.connect(host='localhost',user='root',password='cbytes',database='twitterdatabase')
        
            #Checking if Connection is successful or not 
            if mycon.is_connected():
                print("Successfully connected")
            else:
                print("Not connected")
        
            #Using the cursor object and execute command to count all the tweets in the database  
            cursor=mycon.cursor()
        
            Sentiment_analytical(InputTerm)
            Finalresult=Sentiment_analytical(InputTerm)
            Finalresult_list=[]
        
            tweet_count="Select count(*) from tweets where keyword='{}'".format(InputTerm)
            cursor.execute(tweet_count)
            data=cursor.fetchall()
        
            for iter in Finalresult:
                print("ITER:",iter,"Finalresult:",Finalresult)
                for iterator in iter:
                    pcent=(iterator/data[0][0])*100
                    Finalresult_list.append(round(pcent))
            return Finalresult_list
        
        def Sentiment_analysing(request):
            if request.method=='POST':
                InputTerm=request.POST.get('InputTerm')
                Finalresult_list=Trialfunc(InputTerm)
                print(Finalresult_list)
                print("Length of list:",len(Finalresult_list))
                context1={
                    "Finalresult_list":Finalresult_list
                }
        
                return render(request,'index.html',context1
                )
        
        def Own_tweet_analysis(request):
            if request.method=='POST':
                Input_tweet=request.POST.get('Input_tweet')
                Sentiment_of_tweet=my_own_tweet_analysis(Input_tweet)
                context={
                    "Sentiment_of_tweet":Sentiment_of_tweet  
                }
                return render(request,'index.html',context
                )
#This is the Django file which caters to all the requests of various functions which comes as input from the HTML page
#entered by the user.
