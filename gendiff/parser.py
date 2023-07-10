import argparse
import json
import yaml
from gendiff.formatter import formatter
from gendiff.gendiff import diff
from gendiff.read_files import read_file


def parse_args():
    parser = argparse.ArgumentParser(description="Compares two"
                                                 " configuration files "
                                                 "and shows a difference.")

    # position arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # optional arguments
    parser.add_argument("-f", "--format", help="set format "
                                               "of output", default="stylish")

    args = parser.parse_args()

    # first_file, second_file = read_file(args)
    return args.first_file, args.second_file, args.format


