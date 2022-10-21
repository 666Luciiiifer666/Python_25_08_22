from argparse import ArgumentParser
from utils import *


args = ArgumentParser()

args.add_argument('action', type=str)
args.add_argument('amount', nargs='?')

args = vars(args.parse_args())
action = args.get('action')
amount = args.get('amount')

if action == 'RATE':
    rate(exchange_rate)

elif action == 'AVAILABLE':
    available(usd_available, uah_available)

elif action == 'BUY':
    if amount == 'ALL':
        buy_all(uah_available, exchange_rate, usd_available)
    elif int(amount) > 0:
        buy_xxx(amount, uah_available, usd_available, exchange_rate)

elif action == 'SELL':
    if amount == 'ALL':
        sell_all(usd_available, uah_available, exchange_rate)
    elif int(amount) > 0:
        sell_xxx(amount, usd_available, uah_available, exchange_rate)

elif action == 'NEXT':
    next_step(exchange_rate, delta)

elif action == 'RESTART':
    restart()
