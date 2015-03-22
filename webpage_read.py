# Last Edited (3/21/15)

import urllib2
import random
import anonymize


def readpg(theurl):
    pgreader = urllib2.build_opener()
    response = pgreader.urlopen(theurl).read()

usrurl = raw_input("Enter a url:\n")
readpg(usrurl)
