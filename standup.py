import argparse
import json
import random


def main():
    parser = argparse.ArgumentParser(description='Standup Order Chooser')
    parser.add_argument('--absent', '-a', nargs='+', help='Specify who is absent from standup', action='store')
    args = parser.parse_args()
    absent = [name.lower() for name in args.absent] if args.absent else None
    with open('config.json') as json_file:
        config = json.load(json_file)
    members = [member.lower() for member in config['members']]
    present = [member for member in members if member not in absent] if absent else members
    if present:
        random.shuffle(present)
        print "Today's standup order:"
        for p in present:
            print p.capitalize()
    else:
        print "No one is at standup, so it doesn't really matter what the order is..."


if __name__ == "__main__":
    main()
