from src import main
import argparse
import sys


parser = argparse.ArgumentParser(
    description="Check the strength of your password.")
parser.add_argument('user_input', type=str, help='Input a password', nargs='?')
parser.add_argument("-f",
                    "--file",
                    type=str,
                    default="",
                    help="Username list to report.")

args = parser.parse_args()
test=''


if args.file == "":
    if args.user_input:
       test = main.password_analyser(vars(args)['user_input'])
       print(">>>>>>>>>>>>>>>>>>>>"+ test)
    else:
        parser.print_help()
    # return "Hello from Python!"    

else:
    reader = open(args.file, "r").readlines()

    file = [s.rstrip() for s in reader]
    file.reverse()

    for lines in file:
        print("\nPassword: ", lines)
        main.password_analyser(lines)
    # return "Hello from Python!"
def Function1():
    return "Hello from Python!"