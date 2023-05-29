def my_own_tweet_analysis(my_tweet):
   sid=SentimentIntensityAnalyzer()
   analysis = sid.polarity_scores(my_tweet)

compoundsen=analysis['compound']
if compoundsen<=-0.5000 and compoundsen>=-1.0000:
    Sentiment_of_tweet="Negative"
    score=compoundsen
if compoundsen>-0.5000 and compoundsen<0.0000:
    Sentiment_of_tweet="Weakly Negative"
    score=compoundsen
if compoundsen==0.0000:
    Sentiment_of_tweet="Neutral"
    score=compoundsen
if (compoundsen>0.0000 and compoundsen<0.5000):
    Sentiment_of_tweet="Weakly Positive"
    score=compoundsen
if compoundsen>=0.5000 and compoundsen<=1.000:
    Sentiment_of_tweet="Positive"
    score=compoundsen


return Sentiment_of_tweet,score

The above code is used for the analysis of the tweet entered by the user. First the vader sentiment intensity analyzer analyses the tweet and then based on the compound score , the tweet is categorized into its category. Then the sentiment of tweet and score is returned to the calling function
