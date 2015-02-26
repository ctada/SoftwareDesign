""" Gauge how biased/ opinionated an article is. Extension: Take in a link, parse through webpage. Extension: Gauge how alienating a topic is. 
"""
from pattern.web import *
from pattern.en import *
from math import fabs

# import and parse through text
engine = Bing(license=None) # Enter your license key.
posTotal= 0.0
subTotal = 0.0
variation = 0.0
sentIndex=0
keyterm=raw_input('Enter a search term: ')
for i in range(5):
	for result in engine.search(keyterm, type= SEARCH, cached=False, start=i):
		txt= repr(plaintext(result.text))
		for sentence in txt.split('. '):
			sentIndex+=1
			positivity, subjectivity = sentiment(sentence) 
			posTotal += positivity

			variation = (variation + fabs(positivity))/sentIndex
			subTotal = (subTotal + subjectivity)/sentIndex

print variation, subTotal