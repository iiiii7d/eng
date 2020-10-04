#eng - i____7d
import argparse
import _engcompiler
import traceback
import sys
import colorama

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, nargs='?', help='file to run')
parser.add_argument('-v', '--version', action='store_true', help='check version, then exit')
args = parser.parse_args()

if args.version:
    print("eng " + _engcompiler.VERSION)
    sys.exit()

if args.file == None:
    print("Please input the file that you want to run. For example, 'python eng.py example.eng'")
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
