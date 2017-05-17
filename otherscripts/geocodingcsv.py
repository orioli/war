#!/usr/bin/python

from bs4 import BeautifulSoup
import sys
import re
import csv
import grequests
import time
import json
import math
import csv
import random
import numpy as np

mu = 0.0
sigma = 0.1
# load geocoder
with open('place2lnglat.csv', mode='r') as infile:
    reader = csv.reader(infile)
    geodict = {row[0]:[row[1],row[2]] for row in reader}

#match place to location from geodict
def findlatlon( placename ):
	res = [(k, v) for (k, v) in geodict.iteritems() if k in placename]
	#print res
	if (res and len(res) > 0):
		return res[0][1]
	else:
		return ([42+np.random.normal(mu, sigma, 1)[0],-1+np.random.normal(mu, sigma, 1)[0]])
		
# read csv
with open('../h.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	with open('geoh.csv', mode='w+') as outfile:
		writer = csv.writer(outfile, delimiter=',')
		for row in reader:
			#print ("" + row[5] + "-->" + str(findlatlon(row[5] )))
			deathplacelnglat = findlatlon(row[5])
			row.append(float(deathplacelnglat[0])+np.random.normal(mu, sigma, 1)[0])
			row.append(float(deathplacelnglat[1])+np.random.normal(mu, sigma, 1)[0])

			birthplacelnglat = findlatlon(row[9])
			row.append(float(birthplacelnglat[0])+np.random.normal(mu, sigma, 1)[0])
			row.append(float(birthplacelnglat[1])+np.random.normal(mu, sigma, 1)[0])
			
			writer.writerow( row)