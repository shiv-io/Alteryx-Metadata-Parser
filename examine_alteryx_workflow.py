import xml.etree.ElementTree as ET
from Node import NodeElement
import csv
from shutil import copyfile
import sys

# Input file
file = sys.argv[1]
assert len(file.split('.')) > 1, 'Input file must have an extension'
file_ext = file.split('.')[-1]
assert file_ext == 'xml' or file_ext == 'yxmd', 'Input file must be .xml or .yxmd'
if file_ext == 'yxmd':
    xml = file.split('.')[0] + '.xml'
    copyfile(file, xml)
    tree = ET.parse(xml)
else:
    tree = ET.parse(file)

# Output file
output_file_name = sys.argv[2]
assert len(output_file_name.split('.')) > 1, 'Output file must have an extension'
output_file_ext = output_file_name.split('.')[-1]
assert output_file_ext == 'csv', 'Output file must be .csv'

root = tree.getroot()

lst = []
for x in root.iter('Node'):
    node = NodeElement(x)
    lst.append(node.data)

keys = lst[0].keys()
with open(output_file_name, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(lst)
