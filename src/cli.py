import click
from nse import Nse



@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_equity_price(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price = n.get_data_for_key(data, 'lastPrice')
    print("Current LTP for {} is {}".format(scrip_id, price))



@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_open_price_equity(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price = n.get_data_for_key(data, 'open')
    print("Open Price for {} is {}".format(scrip_id, price))


@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_open_price_equity(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price = n.get_data_for_key(data, 'closePrice')
    print (" Market closes at 4 PM, Close price will be correct after 4PM")
    print("Close Price for {} is {}".format(scrip_id, price))




if __name__ == '__main__':
    #get_equity_price()
    #get_open_price_equity()
    get_open_price_equity()
