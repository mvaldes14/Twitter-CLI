import argparse
import sys
from .helpers import twitter_search, twitter_tweet, twitter_stream


# CLI Interface
def create_parser():
    parser = argparse.ArgumentParser(
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
    if len(sys.argv) <= 1:
        print("No arguments provided")
        sys.exit(1)

    if args.update:
        print("Tweeting...")
        twitter_tweet(args.update)
        print("Done")

    if args.search:
        print("Searching for: " + args.search)
        twitter_search(args.search)

    if args.stream:
        print("Starting Streaming process for: " + args.stream)
        twitter_stream(args.stream)

    elif args is None:
        print('Argument not accepted')
        sys.exit(1)


# Run
if __name__ == "__main__":
    main()
