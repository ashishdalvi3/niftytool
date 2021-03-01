import requests
from bs4 import BeautifulSoup
import lxml, io
import json
import pandas as pd

class Nse:

    def __init__(self):
        self.headers = self.nse_headers()
        self.market_status_url = 'https://www1.nseindia.com//emerge/homepage/smeNormalMktStatus.json'
        self.scrip_csv = 'https://www1.nseindia.com/content/equities/EQUITY_L.csv'
        self.scrip_url = 'https://www1.nseindia.com/corporates/content/securities_info.htm'
        self.scrip_url_old = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={}&illiquid=0&smeFlag=0&itpFlag=0'

    # Returns header which will be used in Requests method
    def nse_headers(self):
        """
        Builds right set of headers for requesting http://nseindia.com
        :return: a dict with http headers
        """
        return { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'Referer': 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=HINDUNILVR&illiquid=0&smeFlag=0&itpFlag=0'
                }

    def get_validate_stock_codes(self,symbol):

        res = requests.get(self.scrip_csv, headers= self.headers)
        #print(res.content)
        df = pd.read_csv(io.StringIO(res.content.decode('utf-8')),index_col=False)
        #symbol_list = df.SYMBOL
        #print(df.loc[df['SYMBOL'] == symbol])
        if (df.loc[df['SYMBOL'] == symbol].empty):
            return False
        else:
            return True 
    

    # This gets full data for any Equity symbol
    def get_scrip_data(self, scrip):

        # Double check to convert symbol code to uppercase
        symbol = scrip.upper()
        print ("Validating Scrip {} ".format(symbol))

        exist_scrip = self.get_validate_stock_codes(symbol)
        if exist_scrip == True:

            print(" Accessing scrip_url " + self.scrip_url_old.format(symbol))
            res = requests.get(self.scrip_url_old.format(symbol), headers = self.headers)

            html_soup = BeautifulSoup(res.text, 'lxml')
            hresponseDiv = html_soup.find("div", {"id": "responseDiv"})
            d = json.loads(hresponseDiv.get_text())
            print(d)
        #print (d.keys())
        #d = json.loads(res.text)['data'][0]
            res = {}
            for k in d.keys():
                v = d[k]
                try:
                    v_ = None
                    if v.find('.') > 0:
                        v_ = float(v.strip().replace(',', ''))
                    else:
                        v_ = int(v.strip().replace(',', ''))
                except:
                    v_ = v
                res[k] = v_

        else:
            print('Invalid Scrip {}'.format(symbol))
            quit()
        return res

    # This will return latest price of Equity stock
    def get_data_for_key (self, data, key):

        price =''
        for k in  data.keys():
            if k == 'data':
                v = data[k]
                for i in v:
                    for price_key in i.keys():
                        if price_key == key:
                            #print(price_key)
                            #print(i[price_key])
                            price = (i[price_key])

            if k == 'lastUpdateTime':
                lastUpdateTime =  (data[k])
                print(lastUpdateTime)


        if price != '' :
            return (price, lastUpdateTime)
        else:
            return 'Price not found'

    # This returns current market status 
    # return type closed or open
    def get_market_status(self):
        
        res = requests.get(self.market_status_url,headers =self.headers)
        content = res.json()
        #print (res.json())
        for k in content.keys():
            status = content[k]
            
            
        return status

    # Returns days high and low for EQ scrip
    def get_day_high_low(self, data):

        print(data)
        for k in  data.keys():
            if k == 'data':
                v = data[k]
                for i in v:
                    for price_key in i.keys():
                        if price_key == 'dayLow':
                            #print(price_key)
                            #print(i[price_key])
                            low = (i[price_key])
                        if price_key == 'dayHigh':
                            high = (i[price_key])

        return (low, high)


'''
if __name__ == "__main__":
    n = Nse()
    data = n.get_scrip_data(self.symbol)
    #print(data)
    price = n.get_current_ltp(data)
    print(price)
'''
