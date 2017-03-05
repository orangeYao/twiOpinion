#coding:utf-8
#!/usr/bin/python

import argparse

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    print type(args)
    print args.data_dir
