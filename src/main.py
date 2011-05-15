'''
Created on May 14, 2011

@author: Dean Chen
'''


if __name__ == '__main__':
    from tradeApi import TradeApi
    
    api = TradeApi()
    print(api.getTicker())
    print(api.getDepth())
    print(api.getTrades())
    
    
    #test comment