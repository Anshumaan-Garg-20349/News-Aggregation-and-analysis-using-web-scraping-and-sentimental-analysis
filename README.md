# News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis
SENTIMENT ANALYSIS

Sentiment analysis (SA) or Opinion Mining (OM) is helpful in solving a vast range of problems that are interest of human and computer interaction experts and specialists. It is also an area of  interest for psychologists, linguists ,advertisers , producers , consumers , and politicians. 

Since the dawn of data , its analysis and the huge volume in which it is generated on daily basis,  it has been of utmost importance that this data be analysed for varied uses that humans need to fulfil there tasks. It is used for analysing sentiment of text passed as a parameter to the analysing function which is mainly based on either the machine learning approach or the lexicon based approach.
The Machine learning based approach uses an algorithm and builds a model by the method of feature selection i.e. by learning from labelled data sets[1]. Some of the popular and most frequently used methods are Naïve Bayes classifiers, Support Vector Machine(SVM) and Random Forest.

The algorithms which are mentioned have the ability to learn every kind of feature for classification by using the criteria of optimization but the problem with ML based algorithms is that the sentiment based classifiers are trained on already pre-feeded labelled data in a particular domain and these then does not work in different domains so to overcome this problem lexicon based methods are preferred over ML based algorithms[2]. 


The approach based on Lexicon provides us with the information that which words and phrases are positive and negative. So Lexicon based approach is nothing but a list consisting of lexical features which are commonly labelled, based on the linguistic orientation , and it is either positive or negative. 
Experts and linguists , for proceeding with lexicon based approach have to initially create a sentiment lexicon by the systematic arrangement and collection of sentiment list of words which is based on corpus based approaches and dictionary based approach. After the list of sentiment words is compiled ,  polarity of the given input , based on the positive and negative indicators is determined which are now known based on the given lexicon. 

The dictionary based approach is achieved by taking a few examples initially and after that any online dictionary can be used for the expansion of sentiment lexicon by including synonyms and antonyms of those words. This dictionary can be filtered by human inspection[2]. The corpus based approach is used to find the sentimental inclination of context based specific words. The following two methods are used under corpus based approach:-

A)	Statistical based approach – If some combination of alphabets comes up with an erratic behaviour but in a beneficial manner , then the overall polarity of the sentence is considered to be positive but if the combination shows a behaviour which is pessimistic in nature then the overall polarity of the sentence changes and tends to have a negative inclination. But if the prevalence of the optimistic and pessimistic text is equal in many ways then the overall polarity tends to have a neutral inclination[12]

B)	Semantic based approach – Under this method , values are assigned to words based on opinion or sentiment and also to the words which are closer to the words to which values are being assigned. This is done by finding synonyms and antonyms to words to which values are assigned[12]

 ![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/cff8ab9b-bb47-49ce-a082-fe273097d1e4)

Under the lexicon approach , some of the lexicons such as GI (General Inquirer) and LIWC ( Linguistic Inquiry and Word Count) classifies the words into the categories of  “POSITIVE” and “NEGATIVE” according to the way of there connotation orientation. 

LIWC has a pool of 4,500 words which have been classified into 76 categories and of them also, approximately 905 words are such which are classified in two categories , particularly related to sentiment analysis .LIWC is a well tabulated and validated lexicon created by more than a decade of  hard-work by experts , specialists , linguists  and psychologists.

Although LIWC has a vast use in defining and redefining words and there sentiment but it lacks a very significant feature which is a very crucial aspect of sentiment analysis when talking in terms of social media such as Twitter i.e. LIWC does not take into account the acronyms, emoticons , initialisms and slangs[2].


There are other lexicons also such as SentiWordNet , SenticNet and ANEW ( Affective Norms for English Words). These type of  lexicons associate with the valence scoring of text for analysing the sentiment intensity. 

The SentiWordNet consists of more than one lakh synsets and these are labelled with sentiment scores categorised as positive , negative and objective. Although it is not as good resource as WordNet still it has varied uses. Lexicon based approach has the biggest advantage that it has its domain independence and above all it can be very easily improved and included in any application 




WEB SCRAPING


In our everyday lives , data is generated in humongous amounts and we need to filter , define and refine this data as per our needs and uses.

But there is a problem , that this data is scattered over this infinite pool called WWW (World Wide Web)[3] , hence the data filtration and refining becomes a problem. Hence we need a tool or maybe a method which let’s us collect this data and the information related to that data at one place , which then could be used for further analysis.

Web scraping or extraction or harvesting is a technique which is used to pull data from the “World Wide Web” and then use it or store as per the requirement. Generally, data on the web is scrapped by using the Hyper text transfer protocol (HTTP) or using a web browser. That can be accomplished by a user(manually) or by the use of a web crawler.

Because humongous amounts of data is continuously being generated on the web , web scraping is a very dynamic and powerful tool for collection of data Today’s scenario is that , web scrapper tools have been modified. From the current human – aided procedures to being developed into fully automated systems which are capable of converting entire website into a dataset , web scrapping tools and methods have changed a lot with time.

Scraping data from the web has two sequential steps i.e. first is the acquiring of web based resources and second is the extraction of desired information from the data that is acquired[3]. First a HTTP request is formulated which can get or acquire the data and information from the selected website. The request which will be sent to the website can be modified in either a URL form which contains a GET query or it could be a HTTP message containing a POST query. 

As and when  the request is received and compiled by the website , the resources which were requested from that website are retrieved and are finally sent back to the program which sent for to get the resources. The data which is received can be in any format be it in HTML[3] ( from which web pages are built) , maybe the data-feeds which are in XML or JSON type format or the received resources may be in multimedia type format such as pictures , audio , videos etc. 

This data ( be it in any form) is first downloaded , after that process of retrieving useful data is initiated by parsing data and information received and during this parsing the data is simultaneously re-formatted and organised in a more presentable format or it can be more conveniently said as structured form of data, is made available.

For web scraping , two modules are very much needed , one module performs the [3]composing of the HTTP requests like the selenium while the other module is needed for the extraction and parsing of information from the basic HTML code using PyQuery or BeautifulSoup. 

VADER


Sentiment analysis describes the definition, description, and evaluation of Valence Aware Dictionary for sEntiment Reasoning which is also known as VADER. 

Sentiment analysis based on Vader is the reform in the identification and designation of the opinions which are expressed by people on social media so that people’s intention can be determined towards any particular event occurred in past , feedback related to a particular product, recommendations given about something or analyse data for some specific use


The user’s intention may be one of the main factors in determining what sentiment will get embedded in the article or review being posted by the user. Vader uses a collection and combination of the evaluative and quantifiable functions to produce and then validate a standard which shines in those names when sentiment lexicons are discussed about and above all this lexicon is very specifically tuned to microblogging type context.

Next comes the compilation of evaluative and quantifiable lexical features with a special emphasis on five generalised rules which will encircle the grammar based and syntax based assumptions and conventions which human beings emphasize upon when expressing the sentiment intensity

Well , to a greater interest and when experimented upon this Vader lexicon , it gave remarkable results and performed very well in the domain of social media and the analysis of posts by people. 

To a greater surprise , it is also showed that individual human raters having a correlation coefficient (r = 0.888) was very much close to the correlation coefficient described by Vader(r=0.881) , this analysis is based on the same ground basis which is the average group mean derived from no less than 20 human raters , performing the analysis of each and every tweet.

And if we proceed with further analysis , the classification frequency of human raters is 0.84 whereas for Vader it is 0.96 , this means that Vader is able to correctly classify tweets into optimistic (positive) , pessimistic(negative) and neutral (positive and negative sentiment intensity is equal).

Vader lexicon features has its own advantages and it also retains  the features of more common lexicons like LIWC , it is much more big in nature but can be simply inspected , can be understood very well and above all it can be applied in a much more faster way with an easy extension

BEAUTIFUL SOUP

Web scraping or extraction or harvesting is a technique which is used to pull data from the “World Wide Web” and then use it or store as per the requirement. Whenever we are discussing about web scraping, web pages is the first thing that comes to our mind because they are storage houses of large amounts of data


A website is a collection of many web pages and it is based on the data which the owner wants to display on the website. Also, there are two types of web pages , one which is static while the other one which is dynamic.

Static web scraping of data or web scraping of data from static web pages is very easy because here we have to send an HTTP request to the server side and the response which we will get, that will be the same page for which the request was sent for and this does not require any extra or more of a complicated process

But if we talk about dynamic web pages and scraping data from them , it is a very complicated process as the dynamic pages on the server side are based on server side scripting languages like Js, ASP, PHP. 

Hence it would be more time taking to load and moreover it is possible that instead of getting a web page for the request that was made , we get a Js code as a response from the side of server. So it can be said that the web scraping that we do , is done by sending an HTTP request to the website and then we get the page source which is then converted to a soup object and then we can get the required elements from it. But if the website was Js rendered which means Js will provide elements which are on the website , then simple sending the HTTP request will not get us the required data[4].

So in the case of Dynamic type web scraping , it is required for the website to get loaded fully , after which the page source is fetched and therefore all the data is then loaded first and then scripting takes place. This way dynamic or the continuously changing data can also be scraped from the web pages



WORKING OF BEAUTIFUL SOUP


This has been used for scraping data from web . It is a python based collection of data stored in the form of a database and it has a base of HTML or XML computational based engine which is used for pulling out , analysing and modifying information which is present in the DOM ( it is basically a cross platform and linguistic independent base which sees HTML and XML documents in the form of a tree type structure and each node of the tree is a object which represents specified part of the whole document) tree of web pages. 

It can send an unparalleled series of unique and concise DOM based visitor interfaces which directly or indirectly helps developers build a system which could be basis for the other models and moreover it has a very special characteristic i.e., across the platform , it can be operated upon, indicating that it is flexible

Clients of Beautiful Soup can, as indicated by their requirements, introduce explicit HTML/XML examination motors (e.g., xml, html5lib, and so forth.). 

Taking lxml for instance, clients can instate Beautiful Soup with the accompanying call: Beautiful Soup (markup,"lxml").Subsequent to instating, Beautiful Soup gets all the relating DOM tree structures for HTML records. 

Then utilizing an inherent series of associated works that relate with DOM API, it visits, gets, and alters the property estimations or sets of the assigned hubs of the DOM tree. Beautiful Soup has not just has an underlying series of DOM API, yet in addition many recently added new interfaces that standard DOM APIs don't have, settling on decisions more straightforward for engineers and developers[4].


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/34f703f9-7e6b-4fcc-a57d-e0e431518f2e)


In most of request interfaces provided by Beautiful Soup (e.g., findPrevious, findPreviousSibling,findParend, findParents, and so forth), all will call the two capabilities _findOne and _findAll, or, in other words that all requests occur inside these two capabilities. At the point when Beautiful Soup characterizes these capabilities, Python's stretching boundary list innovation can complete different DOM API capabilities with an alternate number of boundaries and values to call _findOne and  _findAll, consequently accomplishing two distinct objectives.


For example, _findOne can look through assigned tag or the assigned substance of a tag, while _findAll can look through all labels or content that meet its predefined conditions inside the entire DOM tree


API BASED DATA EXTRACTION

A feature of object-oriented programming languages called an API enables programmers to create software for a specific application using a reference programme library. 

The operating system or application programme of a device specifies the API, via which a requester—another device or a client user—can submit requests and wait for results. APIs provide communication between various software applications and access to their services


NATURAL LANGUAGE TOOLKIT


This NLTK is a naturalised language based processing platform for python which has been developed in the combination of linguistics involving computations in the year 2001 at the Pennsylvania university .

It gives at hand an interface which has 50 corpora and the lexicon based resources which is based on SentiWordNet which has a collection of string and text computing libraries for the lemmatization , classification and tokenization. 

In NLTK , the score based on sentiments is calculated from sentiWordNet which has a table format of polarity score based on each synset in the WordNet categorising it into positive and  negative with the values ranging from 0.0 to 1.0 , in every case the final sum is 1.0 



![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/e6441717-8200-4869-90b1-aa45d87d6add)


PRE-PROCESSING

While doing analysis on tweets ,  they can be pre-processed so that unnecessary data could be filtered out:


1)	Removal of Re-tweets: Re-tweets can be removed from the tweet.

3)	Case sensitive analysis: If we don’t want to use a case sensitive analysis then we can convert upper case words lower case.
4)	Removal of Stop words: All those words which are not carrying any sentiment and also not effect the meaning of the sentence can be removed.
5)	Stemming of words :For filtration of sentences, words can be reduced to there roots and thereby reducing the complexity of sentence in analysis.
6)	Special character and numbers don’t express any sentiments so they can be removed
7)	Slangs and abbreviations can be expanded so that they can be analysed 
8)	Sometimes wrong spellings don’t convey any meaning and sentiments and hence can be discarded
9)	Words can be POS tagged  and hence they can be classified under the headings nouns , adjectives and verbs and hence it involves efficient implementation of analysis 
10)	Removal of username and URL’s can be beneficial as they don’t carry any sentimental value

WORKING OF VADER


Vader is a type of sources package which comes under NLTK.VADER is a tool used to do the sentiment analysis whose approach is lexicon and rule based that is used in the expressions expressed on social media. 

Vader uses a method of scoring which is applied to results after analysing the [2]sentiment of the tweet ( in the case of scrapping tweet from twitter) and as just said we must get the tweet in order to analyse the sentiment of tweet , so for this purpose we use TweePy API , from where we can extract twitter data and by using this we have the real time access to publicly available raw tweets.

Vader includes within it a sentiment lexicon and together with the inclusion of some syntactic rules , the sentiment analysis of text by Vader could be improved. Vader cause of origin is the abbreviations , emojis and slangs used in posts on social media by people and these are like a shorter way of expressing yourself on social media. The syntactic rules used are[2]: 

Emotional intensifying marks: The interrogation and exclamation marks lead to increment and decrement of the sentiment intensity and thus influencing the positive and negative polarity of the text. Eg “This is great !!!” will have a greater positive score as compared to “This is great”[9]

The play of capital text: The intensity of a word which is capitalised in nature and when other words are not capitalised gives a upper hand in intensity to that word when the analysis is performed .Eg “ This is GREAT” will have a greater positive score as compared to “This is great”[9].

Negatory marks: If a word such as “great” gets preceded by a word such as “not” then this could just revert the ongoing positive polarity of the whole sentence and give a negative sentiment. For eg “ The environment is not good here”  will turn the sentiment of the score as negative [9].

Words which gives a boost: There are some words such as “very” and “extremely” which intensify the underlying emotion of the text and this leads to increment in the intensity of the word. Eg “ The environment is good here”  will have a less score as compared to “The environment is very good here” [9].

The contrast creating words such as “but” which can shift the signals of the whole sentence and change the polarity of the text with the sentiment of the text following the contrasting word being the dominating one. Eg “ The environment here is good but it was better in Shimla” has a mixed type of sentiment but the later half of  the sentence is more overpowering [9].

Specifically , in case of Vader lexicon when a sentence or text is passed to the sentient intensity analyser , then the analyser pulls out those words which carry a sentimental value to them and the influence or intensity they have caused to the sentence.[2] 


This lexicon ranges the polarity  from -4 to +4 , where -4 has the maximum negative intensity and +4 has the maximum positive intensity, but when final scoring of the sentence is done then the scores are normalised between -1 and +1 and this standard of normalisation has given this method another name as compound scores.

The compound based score gives us the nature of sentence , talks about its intensity and reviews the polarity. So to give the overall intensity of the sentence , all the polarity scores of sentiment words are added and the normalised scores are thus received:[10]

![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/eb49d2b3-676b-48f2-8a7c-4409fd2bbb0c)


So here x is defined as the sum of polarity scores and alpha is the constant whose numerical value is generally taken as 15. Example – “ The environment here is good and food is nice”. 

Both the words here good and nice have a polarity as 1.9 and 1.8 which on [6]addition gives the value as 3.7 and to get the compound score of the following sentence we do the normalisation and get the answer as 0.6907 , which is between -1 and +1.

Now the categorisation of tweets into various categories happens based on the value of compound score, if the value of compound score is between -0.5 and 0.5 then the tweet is considered as neutral in sentiment and if the value of compound score is greater than 0.5 then it is considered as positive and if the value of the compound score is less than -0.5 then the sentiment of the tweet is considered to be negative


METHODOLOGY

Creation of a virtual environment


Production of a different Virtual Environment for the project is fundamental as it permits the program to introduce and utilize the Python libraries without making any struggles with other programs utilizing similar libraries. It is expected to make the Virtual Environment in a similar organizer as of the whole Project.


Installation of python libraries
The python libraries must be installed by using the Windows PowerShell or by using the IDE terminal (PyCharm). “pip” command is used to install various libraries.


Code editor used for programming 
VS code is used as the code editor for programming. This code editor is very robust and is a good choice for big projects , the only limitation is that it is slow to start up.


Commands used :
1.	python  virtualenv env 
The above command will create a virtual environment 
2.	activate.bat 
The above command will be used for activating virtual environment 

3.	python-admin startproject hello 
The above command will create a project in the vs folder named “hello” and will create many files mainly with “.py” extension and these files are the required files during the making of a Django project.

4.	python  manage.py runserver 
The above command will start the server and a link will be provided to us in the terminal , and on-clicking on that link , we will be redirected to a web page telling us that server is started successfully.


5.	python manage.py startapp mynewapp
The above command is used to make an app ; basically a project contains apps and this command will lead to the creation of an app and contains “.py” files which are required when we make changes in the functionality of the app.

3.6 Django MVT Architecture
The  Model View Template architecture  is a thing arrangement plan. It is a gathering of three gigantic parts Model ,View and Template. The Model assists with managing information base. It is an information access layer which handles the information.

The Template is a show layer which handles User Interface part totally. The View is utilized to execute the business thinking and mark of connection with a model to pass on information and renders an association.

 ![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/55df72eb-f71f-489b-bfb7-3ec13997d904)

Diagram showing the flow of control in Django MVT architecture


   Modules and Functions  Used:
   
   
1)	For Installation: “pip install tweepy”
import tweepy
This module is used for accessing the twitter API and scraping tweets from twitter .

2)	For Installation : “pip install vaderSentiment”
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyser
This module is used for analysing the sentiment of the tweet passed as a parameter to the sentiment intensity analyser.

3)	For Installation : “pip install datetime”
from datetime import timedelta 
from datetime import date
This module is used for getting the current date and saving it with the tweets in the database and timedelta has been used for adding some days to the current date for checking the date of tweet and for how long the tweet has been in the database.

4)	For installation: “pip install mysqlconnector”
import mysql.connector as sqltor
This module has been used to connect my python code with the sql database and to pass strings as sql commands to mysql and fetch the required records and this connector will be referred to as sqltor.

5)	For Installation: “pip install GoogleNews”
from GoogleNews import GoogleNews
This module has been used to get the news along with all the required data of the news.

6)	from django.urls import path,include
This module has been used so that when a request comes , then it could be redirected to the specified app , so basically path function has the parameters for the request and for that request to which app , which has been included in the path function it should be redirected to.

7)	From “app” import views
This tells us that from our app folder we are trying to import views which are basically the main part of MVT architecture and decides how will the data be visible to us. 


8)	from django.shortcuts import render
The Django module is a hub of functions which are commonly used in the context of view type classes.Here the render collects the given template and combines it with the dictionary and finally returns a Httpresponse (object) along with that rendered text.


WORKING


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/de5c799e-7491-4eee-9253-92f0d3cdaf97)


Above image displays the code snippet for web scrapping of news , here first Googlenews class is being imported from GoogleNews python library  and then within the scrapper function , an object of class has been created and then the search keyword inputted by the user is passed to the search function. 

This function searches for the given inputted keyword and then the results function is called  which gives title , link , description , media and date time for the given news and then this result is returned to the calling function.


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/4e7637f0-c4cb-4b6b-831f-0905612d8b00)

Above image shows the authentication handling. Here the access keys are stored in another text file which are accessed using the file read operation. In the file pointer value of every key is being saved as list and  then every key is being allotted its value. After that using the tweepy authentication handler , all four keys are passed as parameters to the functions which basically verifies the authenticity of the user


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/c0c4ec9d-5d21-4acf-8302-c9d404f997f5)


Above image displays that  initially each tweet is scraped using twitter API and then all those scraped Tweets are stored in tweet which  is basically the variable which contains the all the scraped tweets. Each tweet undergoes required pre- processing .i.e. if a tweet has a heading as RT then to clear it , replace function has been used which replaces the heading "RT" with white spaces. 

The importance of doing this is that , now every tweet which has the starting as "RT" will be blank thereafter and hence one word less for analysis. 

Similarly, all the double quotes are also replaced from tweet. Further now sentiment intensity analyser has been used which is basically the object of vader lexicon for calculating the sentiment of tweet and hence this tweet is passed  as a parameter to the polarity_scores method which basically returns the sentiment in a dictionary form: { 'pos' : 0.6575 , 'neg' : -0.6363 , "neu" : 0.6273 , "compound" : 0.7373 }. 

We will be utilizing the ‘compound’ element of the dictionary to classify our tweet into the respective categories.Each category has its individual counter and every time the respective counters are increased by one , whenever the compound score falls in one of the categories. 

Now this data of incremented counter with the respective tweet is added to the database, along with the tweet. For this I have used the sql connector for storing the data of the tweets in the database.


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/ee06dcf6-c9e9-4031-a8ab-25b66e058770)


Above image  shows the deletion of tweets, first the authentication takes place and then the tweets get deleted. Here deletion of tweets have been made because when the same keyword was searched again after the time period of seven days , then if it happens that regarding that same keyword 300 latest new tweets are not  found , then to maintain the number of tweets in the database as 300 only , remaining number of tweets are deleted from the database and now all the new tweets found will be stored in the database with the remaining one’s giving the total count as 300



![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/23ce574f-8bd0-45da-b99f-64ece3d09725)


Above image shows the new tweet count function where first the authentication of user takes place and then we search and count for the new tweets to check whether there are 300 new tweets or not.

For searching, tweepy library’s cursor method is used which has parameter as api.search_tweet which searches for tweets on twitter , second parameter is the keyword regarding which search has to be made , third parameter is the tweet_mode which is set as extended which means  full text tweet will be scraped and nothing will be truncated and all those tweets having language as English.

The items parameter sets the limit for the number of tweets to be scraped or analysed. The results are stored in tweets variable and then iterations are made, with the increment of counter at each step.

RESULTS and DISCUSSION

![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/a54a945f-2f9c-4814-936c-3d3e06a7be32)

displays the first view of the of the website where the Name of the website is being displayed as “Real News” and for this heading tag has been used.

Now below this is the slider which has been added , there are 3 sliders and  the three slides have different pictures and different text is being displayed on each of them. The other two slides are as follows:-

![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/7e835675-8262-450e-b2fe-1c10d32ca810)

![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/a15bc554-62f2-4ab4-b8be-0183969ab3ba)


Above images are the other two sliders and for inserting pictures “img” tag has been used and link of each picture has been provided in the src attribute , and also the dimensions are adjusted as per the requirements. 

The text inserted on each slide is added with the help of style heading tag and font settings have been edited by using the style attribute , the colour and size has been changed. The bold tag has been used for making the heading in each slide as bold

News Aggregator 


![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/180cd01f-da4c-4c02-9b55-f1a04486bc3e)


Above image shows that container is separately enclosed under a div tag and contained within the class attribute and now the <h2> has been used for displaying the heading as “MyNews” and  the user has to enter the keyword of his choice in search bar and then hit enter or click submit button. Here to take input , form tag has been used which returns the input keyword to the program at the backend. 
  
Now the heading “ Search Your Keyword” , search bar and submit button are all inside the jumbotron component of Bootstrap.
 
  
![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/e3ecfa10-cc6c-4dea-a878-3eaf89cfee52)

  
 Above image shows that when the keyword was searched for, then that keyword was passed as a input to the program at the backend and the output of the program was passed as a input to the website and displayed. 
  
Whenever news will be scraped , along with that all the data related to that news such as title , Media , date-time , Description , Link and Duration(When was it published on the site from where it is scraped). All these top 10 news are displayed in a separate jumbotron and an internal scroll bar is added for scrolling down to every news.
  
  
SENTIMENT ANALYSIS 

![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/99d13605-3320-45e2-a096-011dfb5c400e)

  
Above image shows that  heading “Sentimental analysis” is added with the help of heading tag and within the jumbotron heading “Search your keyword” has been added , user can enter the keyword in the search bar and then click on the submit button. 
  
The input term is passed as a input to the program at the backend and the results are fetched and displayed on the website.
  
 ![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/ee3f000e-bb58-43d8-9552-f8a755810c91)

 Above image shows that  the “Results:” heading is again inserted using the heading tag and with a limit of around 300 tweets , analysis of each tweet is performed and with the classification of each tweet into respective categories , we get the results. The respective categories and the above written statement in the screenshot are enclosed within a jumbotron.
  
  
![image](https://github.com/Anshumaan-Garg-20349/News-Aggregation-and-analysis-using-web-scraping-and-sentimental-analysis/assets/74877493/18fdcdfd-f569-4f10-9bb4-3b3bc977cda5)

  
Above image shows  the analysis of the tweets which the user wishes to post on twitter and in the above screenshots , in one of the screenshots simple statement is inputted “Smile is good” while in the other screenshot statement with the emoticon has been used “ :-) is good” .
  
Vader gives the same polarity score to both the statements and hence Vader proves that it is an ideal case to be used for sentiment analysis in the context of social media.
  
 ADVANTAGES:
1)	News is live scraped so there is no delay of news.
2)	It is flexible in nature in the sense that more news i.e. greater than 10 could be scraped off , region could be specified , language can be added as a parameter and by clicking on links directly the user will be redirected to the news web-page.
3)	User now could be made aware of the on-going public sentiment regarding any specific topic.
4)	User can know the sentiment and message his tweet will convey to others on social media.
5)	It will help prevent rumours and the spreading of false information among people
6)	It will help an individual realize whether and what to comment about socially sensitive topics


  
 DIS-ADVANTAGES:
1)	It takes a bit long to scrape news.
2)	It takes long to scrape tweets , if the entered keyword is not previously present in the database.
3)	Sometimes the length of tweet is too long to get saved in the database and hence this gives an error 
4)	The authentication handler function didn’t work and because of that each function which scrapes tweets using twitter API needs authentication , the code of that function had to be repeated.
5)	The current program is not able to scrape the date at which the tweet was posted on twitter.
6)	In the case of web scraping , images are not scraped with the  required news and sometimes date time parameter returns none.
  
CONCLUSIONS AND FUTURE WORK
  
As the internet has grown exponentially and markets are , in today’s world totally data dependent, it is now a necessity to have access to the updated and latest data be it in any field. Data is the main decision making factor and the cause that any business can run profitably or not. 
  
  In the era of today , every person can find the growth and emergence of a new factor every year and web scraping is no different from it. This factor has its foundation built on the basis of structured and unstructured data. In the case of news also, people can save so much of there time by using news aggregators instead of looking individual news sites on the web. News aggregators collect all the data related to a particular news item at one place and thus help save a lot of time for the users.
  
  
Twitter sentimental analysis falls under the headline of mining of text and opinions and here focus is on the analysis of tweets and to present the results under different categories and sub-categories. 
  
  These results can help to analyse and forecast customer behaviour towards any product and his relationship with the producer , analysis of comments on various social media handles or helping a political party decide which way to pave for diverting the views of public based on the on-going public sentiment. 
  
  The full process of analysis involves collecting data , sentiment analysis and then its classification. To some extent it also involves pre-processing of tweets but in the context of Vader which is built especially for social media handles where people mostly are interested in using short forms , slangs and emojis have a very intense influence on the sentiment intensity of the overall tweet and if pre-processing done then all of these will be removed off from the sentence maybe due to non-understandability of the short forms or short forms and slangs being seen as spelling errors.
  
With the changes in this field and the on-going development , slowly but surely models of analysis will come which will have high accuracies.
  
  
FUTURE WORK
  
  
Both web scraping and sentiment analysis have immense scope in the future. Web scraping can be more refined and can target specific information which the user has demanded and moreover the current flaws within the existing modules must also be resolved to make them more efficient. 
  
To improve web scraping specific functions can be added to scrape images and date-time which is not appearing in some instances must be visible in every instance then. 
  
Secondly , the sentiment analysis part can analyse the sentiment of the text, and Vader , which is a lexicon based analysis tool specially made for analysing the sentiments of posts by people on social media has a very high level of accuracy and is at par with human raters for analysis. 
  
Here the time which is required to scrape new tweets can be improved and for authentication handling a specific function must be made which will reduce code repetition and save time while debugging.

