import argparse

def format_price(price):
    if price is None:
        raise ValueError
    if not str(price).replace('.','').isdigit():
        raise ValueError
    price = float(price)
    if price.is_integer():
        return '{:,.0f}'.format(price).replace(',', ' ')
    return '{:,.2f}'.format(price).replace(',', ' ')



def get_args():
    parser = argparse.ArgumentParser(description='pretty view of price')
    parser.add_argument('price', help='price to convert')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    print(format_price(args.price))