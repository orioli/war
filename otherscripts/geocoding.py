#!/usr/bin/python

from bs4 import BeautifulSoup
import sys
import re
import csv
import grequests
import time
import json
import math

YOUR_API_KEY = "AIzaSyAXkI6aCV58GQ89uIDFxInOy53egAvB0BQ"
place = ["Berlin","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid","Gusen","Madrid"]
chunk_size = 1

current_place = "xx"
def process_a_page(response, *args, **kwargs): 
	geodata = json.loads(response.content)
	##print (geodata)
	lat = geodata['results'][0]['geometry']['location']['lat']
	lng = geodata['results'][0]['geometry']['location']['lng']
	print(current_place+","+str(lat) + "," + str(lng))

def geocode(k):
	x = "https://maps.googleapis.com/maps/api/geocode/json?address="
	x2 = "&key="+YOUR_API_KEY
	URLS = [x+place[k]+x2]
	reqs = [grequests.get(url, hooks={'response': process_a_page}) for url in URLS]
	resp = grequests.map(reqs, size=chunk_size)


with open('places_clean.txt') as f:
    place = f.readlines()


place = place[::-1]

for k in range(671, len(place)):
	##print("geocoding  ",str(k))
	##print("")
	##sys.stdout.flush()
	current_place =''.join(place[k].splitlines())
	geocode(k)
	time.sleep(3)

