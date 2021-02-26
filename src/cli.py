import click
from nse import Nse



@click.command() # type: ignore
@click.option('-s', '--symbol')
def get_equity_price(symbol):
    scrip_id = symbol.upper()
    n = Nse()
    data = n.get_scrip_data(scrip_id)
    price = n.get_current_ltp(data)
    print("Current LTP for {} is {}".format(scrip_id, price))



if __name__ == '__main__':
    get_equity_price()

