import pickle
import datetime
import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help='Num last N messages to list', default=10)
parser.add_argument('pickle_file', nargs='?', default='message_history.pickle') 
args = parser.parse_args()

with open(args.pickle_file, 'rb') as f:
    # open -> sort -> slice
    messages = sorted(pickle.load(f).values(), key=lambda x: x['timestamp'], reverse=True)[:args.n]
    
    # unix timestamp to human readable
    for message in messages:
        message['timestamp'] = datetime.datetime.fromtimestamp(message['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    
    print(tabulate(messages))
