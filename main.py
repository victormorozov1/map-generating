import argparse
from map import Map


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int, default=256)
    parser.add_argument('-c', '--clouds', action='store_true')
    parser.add_argument('-nw', '--no_water_around', action='store_true')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    map = Map(args.size, make_clouds=args.clouds, water_around=(args.no_water_around + 1) % 2)
    map.show()


if __name__ == '__main__':
    main()