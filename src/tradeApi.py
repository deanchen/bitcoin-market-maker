'''
Created on May 15, 2011

@author: Dean Chen
'''

import json
import urllib.request

class TradeApi(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''API URL: https://mtgox.com/support/tradeAPI'''
        self.TICKER_URL = 'https://mtgox.com/code/data/ticker.php'
        self.DEPTH_URL = 'http://mtgox.com/code/data/getDepth.php'
        self.TRADES_URL = 'http://mtgox.com/code/data/getTrades.php'
        
    def getTicker(self):
        tickerJson = urllib.request.urlopen(self.TICKER_URL).read().decode()
        return json.loads(tickerJson)
        
    
    def getDepth(self):
        depthJson = urllib.request.urlopen(self.DEPTH_URL).read().decode()
        return json.loads(depthJson)
    
    def getTrades(self):
        tradesJson = urllib.request.urlopen(self.TRADES_URL).read().decode()
        return json.loads(tradesJson)
       
        
        
        