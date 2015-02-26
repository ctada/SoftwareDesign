from pattern.web import *
g = Google()
t = Twitter()
i = None
#keyterm = raw_input() # #Євромайдан #Евромайдан #Euromaidan
for j in range(3):
    for tweet in t.search(raw_input(), start=i, count=10):
        txt = tweet.text
        inEng = g.translate(txt, input=g.identify(txt), output='en', cached=False) # language codes available here: http://en.wikipedia.org/wiki/Template:Google_translation
        i = tweet.id
        print txt
        print inEng

#for trend in Twitter().trends(cached=False):
#	tweet = Twitter().stream(trend)
#	for i in range(10):
#		time.sleep(1)
#	    tweet.update(bytes=1024)



# gauge interest across languages/ countries (frequency counter)


# sentiment analysis (based on English translation?)

