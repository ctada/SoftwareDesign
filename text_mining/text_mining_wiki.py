""" Measure how degree of translation (measured in times that an article has been translated) affects Pattern's sentiment analysis
"""
from pattern.web import *
from pattern.en import *
from math import fabs
from random import randint

def translate_mult(n=0):
	""" Ask for search term, and translate Wikipedia article through random series of languages n times. 
		Track how Pattern's measure of subjectivity changes with each translation
	"""
	# initialize engines
	w= Wikipedia(license=None)
	g= Google(license=None, throttle=0.5, language=None)

	# create list of language codes supported by Google Translate
	languages = "af, ach, ak, am, ar, az, be, bem, bg, bh, bn, br, bs, ca, chr, ckb, co, crs, cs, cy, da, de, ee, el, en, eo, es, es-419, et, eu, fa, fi, fo, fr, fy, ga, gaa, gd, gl, gn, gu, ha, haw, hi, hr, ht, hu, hy, ia, id, ig, is, it, iw, ja, jw, ka, kg, kk, km, kn, ko, kri, ku, ky, la, lg, ln, lo, loz, lt, lua, lv, mfe, mg, mi, mk, ml, mn, mo, mr, ms, mt, ne, nl, nn, no, nso, ny, nyn, oc, om, or, pa, pcm, pl, ps, pt-BR, pt-PT, qu, rm, rn, ro, ru, rw, sd, sh, si, sk, sl, sn, so, sq, sr, sr-ME, st, su, sv, sw, ta, te, tg, th, ti, tk, tl, tn, to, tr, tt, tum, tw, ug, uk, ur, uz, vi, wo, xh, xx-bork, xx-elmer, xx-hacker, xx-klingon, xx-pirate, yi, yo, zh-CN, zh-TW, zu"
	languages = languages.split(", ")
	languages = list(zip(range(1,len(languages)+1), languages))

	# initalizations of variables
	posTotal= 0.0
	subTotal = 0.0
	variation = 0.0
	sentIndex=0
	keyterm = "Russia"
	#keyterm=raw_input('Enter a search term: ')

	article= w.search(keyterm)
	txt= repr(article.plaintext())

	#translate multiple times
	for transIt in range (n):
		txt= g.translate(txt, input=g.identify(txt)[0], output=languages[randint(1, len(languages)+1)], cached=False)  #translate to random language
		# sentiment analysis per sentence, average over full article
		for sentence in txt.split('. '):
			sentIndex+=1
			positivity, subjectivity = sentiment(sentence) 
			print positivity, subjectivity
			posTotal += positivity
			variationTot += fabs(positivity)
			subTotal += subjectivity

			variation = variationTot/sentIndex  # averages variation each time
			avgSubject= subTotal/sentIndex		


translate_mult(3)