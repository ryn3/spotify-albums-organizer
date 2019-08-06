import xmltodict
import pprint
import json

with open('master_part_ac') as fd:
    doc = xmltodict.parse(fd.read())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(doc))