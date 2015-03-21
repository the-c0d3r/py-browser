# Last Edited (3/21/15)

import urllib2, random, anonymize

def readpg():
    pgreader = urllib2.build_opener()
    response = pgreader.open(usrurl)
    
usrurl = raw_input("Enter a url:\n")
readpg(usrurl)
