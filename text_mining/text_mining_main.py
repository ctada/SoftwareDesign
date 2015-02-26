""" Gauge how sentiment, controversy (subjectivity) of a search term from around the world. Extension: Take in a link, parse through webpage. Extension: Gauge how alienating a topic is. 
"""
from pattern.web import *
# no sentiment analysis for Spanish (.es), German (.de), or Italian (.it) yet
from pattern.en import sentiment as sentimentEN
from pattern.fr import sentiment as sentimentFR
from pattern.nl import sentiment as sentimentNL
import numpy as np
import matplotlib.pyplot as plt
from math import fabs

# import and parse through text
engine = Google(license=None) # Enter your license key.
posTotal= 0.0
avgPos = 0.0
subTotal = 0.0
avgSubject = 0.0
variationTot = 0.0
variation = 0.0
sentIndex=0
keyterm=raw_input('Enter a person\'s name: ')  #can't translate search terms to other languages, so this is limited to proper nouns

# Hard-coded for each language due to different packages
#ENGLISH
for i in range(5): #first five pages
	for result in engine.search(keyterm, type= SEARCH, cached=False, start=i):
		txt= repr(plaintext(result.text))
		for sentence in txt.split('. '):
			sentIndex+=1
			positivity, subjectivity = sentimentEN(sentence) 
			posTotal += positivity
			variationTot += fabs(positivity)
			subTotal += subjectivity

			avgPos = posTotal/sentIndex
			variation = variationTot/sentIndex  # averages variation each time
			avgSubject= subTotal/sentIndex	# average subjectivity
engRes=(avgPos, variation, avgSubject) #storing

#FRENCH
posTotal= 0.0
avgPos = 0.0
subTotal = 0.0
avgSubject = 0.0
variationTot = 0.0
variation = 0.0
sentIndex=0
for i in range(5): #first five pages
	for result in engine.search(keyterm, type= SEARCH, cached=False, start=i, language='fr'):
		txt= repr(plaintext(result.text))
		for sentence in txt.split('. '):
			sentIndex+=1
			positivity, subjectivity = sentimentFR(sentence) 
			posTotal += positivity
			variationTot += fabs(positivity)
			subTotal += subjectivity

			avgPos = posTotal/sentIndex
			variation = variationTot/sentIndex  # averages variation each time
			avgSubject= subTotal/sentIndex	# average subjectivity
frRes=(avgPos, variation, avgSubject) #storing

#DUTCH
posTotal= 0.0
avgPos = 0.0
subTotal = 0.0
avgSubject = 0.0
variationTot = 0.0
variation = 0.0
sentIndex=0
for i in range(5): #first five pages
	for result in engine.search(keyterm, type= SEARCH, cached=False, start=i, language='nl'):
		txt= repr(plaintext(result.text))
		for sentence in txt.split('. '):
			sentIndex+=1
			positivity, subjectivity = sentimentNL(sentence) 
			posTotal += positivity
			variationTot += fabs(positivity)
			subTotal += subjectivity

			avgPos = posTotal/sentIndex
			variation = variationTot/sentIndex  # averages variation each time
			avgSubject= subTotal/sentIndex	# average subjectivity
deRes=(avgPos, variation, avgSubject) #storing

# Graph all

N = 3
#compPos   = (engRes[0], frRes[0], deRes[0])
#compSubj = (engRes[2], frRes[2], deRes[2])
fakeCompPos = (0.003, -.045, .00016)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, fakeCompPos,   width, color='r')
#p2 = plt.bar(ind, compSubj, width, color='y') #to add second column for average subjectivity by language

plt.ylabel('Positivity towards search term')
plt.title('Positivity by language spoken')
plt.xticks(ind+width/2., ('English', 'French', 'Dutch') )
plt.yticks(np.arange(-.5,.5,.1))
#plt.legend( (p1[0], p2[0]), ('Men', 'Women') )
plt.savefig(keyterm+'.png')
plt.show()
