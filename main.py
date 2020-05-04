import yaml
import csv
import os


def csv_to_yaml(input_csv, output_yaml):
    f = open(input_csv, 'r')
    out = open(output_yaml, 'w+')
    for line in f.readlines():
        if not line.startswith(';'):
            print(line)
            out.write(line.replace(';', ':'))
