import argparse
import sys
from .helpers import twitter_search, twitter_tweet, twitter_stream


# Subclass Argparser to fail on unknown argument
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """
        Custom error function to exit with code 2 and limit the output the user sees.
        """
        self.exit(2, 'Error, see --help for valid arguments')


# CLI Interface
def create_parser():
    """
    Create parser object with defined arguments
    """
    parser = CustomArgumentParser(
        description="Twitter CLI Client",
        usage='Search, Update or Stream your favorite data from Twitter', add_help=True)
    parser.add_argument('-u', dest="update", help="Tweet something")
    parser.add_argument('-s', dest="search", help="Search for tweets")
    parser.add_argument('-t', dest="stream",
                        help="Start the streaming process")
    parser.add_argument('--export', help='Export Twitter data')
    return parser


# Main
def main():
    parser = create_parser()
    args = parser.parse_args()

    if len(sys.argv) == 1:
        sys.stdout.write("No arguments provided")
        sys.exit(2)

    if args.update:
        sys.stdout.write("Tweeting...")
        twitter_tweet(args.update)
        sys.stdout.write("Done")

    if args.search:
        sys.stdout.write("Searching for: " + args.search + "\n")
        twitter_search(args.search)

    if args.stream:
        sys.stdout.write(
            "Starting Streaming process for: " + args.stream + "\n")
        twitter_stream(args.stream)
