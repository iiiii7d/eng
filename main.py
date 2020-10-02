import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='f', type=str, nargs='?', help='file to run')

args = parser.parse_args()
print(args.file)