import argparse

parse = argparse.ArgumentParser(description="test")

parse.add_argument('count', action='store', type=int)
parse.add_argument('units', action='store')
# parse.add_argument('price', action='store', type=float)
# parse.add_argument('meter', action='store')

print(parse.parse_args())
