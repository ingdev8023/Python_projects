import argparse
from pathlib import Path
import csv
import os

parser = argparse.ArgumentParser()
parser.add_argument('path',type=str, help='This should be the folder path')
args = parser.parse_args()
print(args.path)
p = Path(args.path)
first_list = [x for x in p.iterdir()]
print(first_list)

   

""" with open('manifest.csv', 'w') as manifest:
    writer = csv.writer(manifest)
    writer.writerow(first_list) """


