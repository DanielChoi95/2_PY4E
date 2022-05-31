import re

file_name= input("Enter file name: ")
fh= open(file_name)
data=fh.read()

x= re.findall('\d+', data)
x_int= [int(i) for i in x]
print(sum(x_int))

###################################################
import socket
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80)) #host, port

cmd= 'GET http:///data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

####################################################

import urllib.request, urllib.parse, urllib.error

fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts= dict()
for line in fhand:
    words= line.decode().split()
    for word in words:
        counts[word]= counts.get(word, 0) +1
print(counts)

##################################################

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url= input('Enter URL : ')
html= urllib.request.urlopen(url).read()
soup= BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags= soup('a')
for tag in tags:
    print(tag.get('href', None))

###################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
sum_tags= 0
for tag in tags:
    content= int(tag.contents[0])
    sum_tags= sum_tags+content
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

print(sum_tags)

####################################################3

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
uh = urlopen(url, context=ctx)
data = uh.read()
xml=data.decode()
tree = ET.fromstring(xml)
counts= tree.findall('.//count')

sum=0
for count in counts:
    sum=sum+int(count.text)

print(sum)

###############################################################

import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
uh = urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)

#print('User count:', len(info['comments']))

sum=0
for user in info['comments']:
    sum= user['count']+sum
print(sum)

###################################################

import urllib.request, urllib.parse, urllib.error
import json
import ssl

from numpy import place

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    #debugging
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(js)
    #print(json.dumps(js, indent=4))
    place_id= js['results'][0]['place_id']
    print(place_id)