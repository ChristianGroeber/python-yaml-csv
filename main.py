import yaml
import csv
import os


def csv_to_yaml(input_csv, output_yaml, encoding='utf-8'):
    f = open(input_csv, 'r', encoding=encoding)
    out = open(output_yaml, 'w+')
    for line in f.readlines():
        if not line.startswith(';'):
            print(line)
            out.write(line.replace(';', ': '))
