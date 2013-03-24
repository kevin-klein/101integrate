#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import csv

resNames = sys.argv[3:-1]
print resNames
datafolder = sys.argv[1]
mappings = {}
for resName in resNames:
	rawmapping = csv.reader(open(datafolder + sys.argv[2]  + resName + "/metadata/mapping.csv"), delimiter=',')
	mapping = {}
	for row in rawmapping:
		print row[0]
		if row[0] == 'TERM' and row[2]:
			mapping[row[2]] = row[1]
	mappings[resName] = mapping

f = open(datafolder + sys.argv[-1] + "mapping.json", 'write')
f.write(json.dumps(mappings))