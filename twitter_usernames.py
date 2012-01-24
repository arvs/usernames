import sys
import string
import requests

names = []
letters = list(string.lowercase)
for c1 in letters:
    for c2 in letters:
        for c3 in letters:
            names.append(c1+c2+c3)
        
avail = [name for name in names if requests.get("https://api.twitter.com/1/users/show.json?screen_name=" + name).status_code == 404]
print "Available:"
avail