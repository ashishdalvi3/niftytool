import click
from nse import Nse



@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_equity_price(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price, lastUpdateTime = n.get_data_for_key(data, 'lastPrice')
    print("Current LTP for {} is {} at time {} ".format(scrip_id, price, lastUpdateTime))



@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_open_price_equity(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price, lastUpdateTime = n.get_data_for_key(data, 'open')
    print("Open Price for {} is {} at time {} ".format(scrip_id, price, lastUpdateTime))


''' Commenting this for now 
@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_close_price_equity(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    market_status = n.get_market_status()
    if market_status == 'closed':
        data = n.get_scrip_data(scrip_id)
        ( price, lastUpdateTime ) = n.get_data_for_key(data, 'closePrice')
        print("Close Price for {} is {} at time {}".format(scrip_id, price, lastUpdateTime))
    else:
        print( "Market closes at 4 PM, Close price will be available after 4PM")

'''

@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_day_high_low(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    low, high = n.get_day_high_low(data)
    print(" Days Low is {} and Days High is {} ".format(low, high))

@click.command() # type: ignore
def is_market_open():

    n = Nse()
    market_status = n.get_market_status()
    print("Market is {} currently ".format(market_status))

if __name__ == '__main__':
    #get_equity_price()
    get_day_high_low()
    # get_open_price_equity()
    #get_close_price_equity()
    #is_market_open()
