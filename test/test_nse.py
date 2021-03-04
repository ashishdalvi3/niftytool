import unittest
import logging
import json
from src.nse import Nse

headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'accept-language': 'en,gu;q=0.9,hi;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'Referer': 'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=HINDUNILVR&illiquid=0&smeFlag=0&itpFlag=0'
                }

scrip_csv = 'https://www1.nseindia.com/content/equities/EQUITY_L.csv'

class TestNse(unittest.TestCase):



    def test_get_validate_stock_codes_pass(self):
        self.scrip_csv = scrip_csv
        self.headers = headers
        p = Nse.get_validate_stock_codes(self,"RELIANCE")
        self.assertEqual(p,True)


    def test_get_validate_stock_codes_fail(self):
        self.scrip_csv = scrip_csv
        self.headers = headers

        p = Nse.get_validate_stock_codes(self,"REL")
        self.assertEqual(p,False)


    def test_nse_headers(self):
        header = Nse.nse_headers(self)
        self.assertEqual(header, headers)

