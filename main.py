import argparse
import logging

from parser import Parser


def run():
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--country', type=str, required=True)
  parser.add_argument('-n', '--universe', type=int, required=True)
  parser.add_argument('-u', '--user', type=str, required=True)
  parser.add_argument('-p', '--password', type=str, required=True)
  parser.add_argument('-v', '--verbose', action='store_true')
  args = parser.parse_args()

  if args.verbose:
    logging.basicConfig()
    logging.getLogger('bogame').setLevel(logging.DEBUG)
  parser = Parser(args.country, args.universe, args.user, args.password)
  parser.parse_all()
  parser.print_debug()


if __name__ == '__main__':
  run()
