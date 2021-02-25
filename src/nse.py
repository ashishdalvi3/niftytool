import requests
from bs4 import BeautifulSoup
import lxml
import json

class Nse:

    def __init__(self):
        self.headers = self.nse_headers()
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



    # future work to get scrip details everytime
    def validate_scrip(self):

        return None

    def get_scrip_data(self, scrip):

        print(" Accessing scrip_url " + self.scrip_url_old.format(scrip))
        res = requests.get(self.scrip_url_old.format(scrip), headers = self.headers)


        html_soup = BeautifulSoup(res.text, 'lxml')
        hresponseDiv = html_soup.find("div", {"id": "responseDiv"})
        d = json.loads(hresponseDiv.get_text())
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
        return res

    # This will return latest price of Equity stock
    def get_current_ltp(self, data):

        for k in  data.keys():
            if k == 'data':
                v = data[k]
                for i in v:
                    for price in i.keys():
                        if price == 'lastPrice':
                            price = (i[price])

        if price != '' :
            return price
        else:
            return 'Price not found'

if __name__ == "__main__":
    n = Nse()
    data = n.get_scrip_data('RELIANCE')
    #print(data)
    price = n.get_current_ltp(data)
    print(price)