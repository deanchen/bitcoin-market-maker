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
        '''
        Constructor
        '''

    if __name__ == '__main__':
        '''API URL: https://mtgox.com/support/tradeAPI'''
        TICKER_URL = 'https://mtgox.com/code/data/ticker.php'
        DEPTH_URL = 'http://mtgox.com/code/data/getDepth.php'
        TRADES_URL = 'http://mtgox.com/code/data/getTrades.php'
        
        tickerJson = urllib.request.urlopen(TICKER_URL).read().decode();
        print(json.loads(tickerJson));
        
        depthJson = urllib.request.urlopen(DEPTH_URL).read().decode();
        print(json.loads(depthJson));
        
        tradesJson = urllib.request.urlopen(TRADES_URL).read().decode();
        print(json.loads(tradesJson));
        