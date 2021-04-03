import requests
from bs4 import BeautifulSoup
class Bse:
      def __init__(self,symbol):
            googleUrl=f'https://www.google.co.in/search?q=bse+{symbol}+stock+price'
            self.soup=self.getScrapedWebsite(googleUrl)
            allLinks=self.soup.find_all('a')
            hreflinks=map(lambda x:x.get('href'),allLinks)
            REQUIRED_LINK_INDEX=0
            REQUIRED_SPLITED_LINK_INDEX=1
            bseIndialink=[*filter(lambda x:x.find('bseindia.com')!=-1,hreflinks)][REQUIRED_LINK_INDEX].split('=')[REQUIRED_SPLITED_LINK_INDEX]
            self.bseIndiaResultPage=self.getScrapedWebsite(bseIndialink,includeHeader=True)
      def getDayHighAndLow(self):
            allSpanTags=self.soup.find_all('span')
            allSpanTagsTexts=map(lambda x:x.text,allSpanTags)
            DAY_HIGH_AND_LOW_INDEX=0
            return ''.join([*filter(lambda x:x.find(' to ')!=-1,allSpanTagsTexts)])
      def getMarketStatus(self):
            allStrongTags=self.bseIndiaResultPage.find_all('strong')
            MARKET_STATUS_INDEX=2
            return [*map(lambda x:x.text,allStrongTags)][MARKET_STATUS_INDEX]
      def getScrapedWebsite(self,url,includeHeader=False):
            headers = {
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0"
            }
            try:
                  if(includeHeader):
                        response=requests.get(url,headers=headers)
                  else:
                        response=requests.get(url)
            except:
                  raise Exception("Unable to connect to servers .Please check your internet connection ")
            soup=BeautifulSoup(response.text,"lxml")
            return soup

# To enovke the class
# bse=Bse('tatamotors')
# print(bse.getDayHighAndLow())