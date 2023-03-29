import argparse
import datetime as dt
from auto_writter import auto_writter

parser = argparse.ArgumentParser()

# Arguments
parser.add_argument(
    "-r",
    "--record",
    action='store_true',
    help="Record the screen"
)

args = parser.parse_args()

def main():
    auto_writter(args.record)

if __name__ == "__main__":
    main()