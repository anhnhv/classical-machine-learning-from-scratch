#!/usr/bin/env python3

import argparse
from main import load_raw_data, raw_data_to_datasets, write_datasets

def raw2dataset(args):
    raw_data = load_raw_data(args.input)
    datasets = raw_data_to_datasets(raw_data)
    write_datasets(args.output, datasets)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Data processing scripts')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # raw2dataset subcommand
    raw2dataset_parser = subparsers.add_parser('raw2dataset', help='Process raw data and create datasets')
    raw2dataset_parser.add_argument('input', help='Input file path (e.g., raw-data/train.tsv)')
    raw2dataset_parser.add_argument('output', help='Output file path pattern (e.g., datasets/train-{lines}.txt)')
    raw2dataset_parser.set_defaults(func=raw2dataset)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()