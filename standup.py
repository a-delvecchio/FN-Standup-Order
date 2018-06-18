import argparse
import json
import random


def main():
    """
    Main CLI function
    """
    parser = argparse.ArgumentParser(description='Standup Order Chooser')
    parser.add_argument('--absent', '-a',
                        help='Specify who is absent from standup',
                        action='store')
    args = parser.parse_args()
    absent = args.absent.lower() if args.absent else None
    with open('config.json') as json_file:
        config = json.load(json_file)

    present = [member for member in config['members'] if not absent or member not in absent]
    start_with = random.choice(present)
    direction = random.choice(['left', 'right'])

    print "Start with {} and go {}".format(start_with, direction)


if __name__ == "__main__":
    main()
