#eng - i____7d
VERSION = "v0.2 (3/10/20)"

import argparse
import _engcompiler
import traceback
import sys
import colorama

parser = argparse.ArgumentParser()
parser.add_argument('file', metavar='f', type=str, nargs='?', help='file to run')
args = parser.parse_args()

if args.file == None:
    print("Please run this script in the command prompt instead of the python shell. Example: 'python main.py example.eng'")
    sys.exit()

try:
    if not args.file.endswith(".eng"):
        print(_engcompiler.error("0.1", 0).replace("<fileName>", args.file))
    else:
        _engcompiler.compiler(args.file)
except Exception as e:
    if e == KeyboardInterrupt:
        print("exited")
    else:
     print(_engcompiler.error("0.2", 0).replace("<error>", colorama.Fore.YELLOW + traceback.format_exc()))