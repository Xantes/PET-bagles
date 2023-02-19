import argparse
from app import main

parser = argparse.ArgumentParser("Lobby Guy")
parser.add_argument('-t', '--type', required=True)
parser.add_argument('-r', '--session_id')
parser.add_argument('-n', '--number')

args = parser.parse_args()

if args.type == 'new_game':
    main()
elif args.type == 'guess':
    if args.session_id and args.number:
        print("Trying to guess the number")
    else:
        print('Not enough argumets')
