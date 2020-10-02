#eng - i____7d
VERSION = "v0.1 (2/10/20)"

import argparse
import _engcompiler
import traceback

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='f', type=str, nargs='?', help='file to run')
args = parser.parse_args()

try:
    if not args.file.endswith(".eng"):
        print(_engcompiler.error("0.1", 0).replace("<fileName>", args.file))
    else:
        _engcompiler.compiler(args.file)
except:
    print(_engcompiler.error("0.1", 0).replace("<error>", traceback.format_exc()))