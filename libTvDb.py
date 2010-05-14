#!/usr/bin/env python

from xml.etree import ElementTree
import urllib2

def getServerTime():
    raw = urllib2.urlopen('http://www.thetvdb.com/api/Updates.php?type=none')
    node = ElementTree.parse(raw)
    return node.find('Time').text
