'''
Created on Aug 26, 2016

@author: xin.li
'''

import urllib2
class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    



