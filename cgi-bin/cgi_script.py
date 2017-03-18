#!/usr/bin/env python3

import recount_of_great_trees
#import matrix
from math import sqrt
import cgi
import json
import cgitb; cgitb.enable()

print("Content-type: application/json")
print("")

form = cgi.FieldStorage()
test = form.getvalue("test")
res = json.loads(test)


matrix_lin = res["data"]

n = int(sqrt(len(matrix_lin)))
graph = [[0 for j in range(n)] for i in range(n)] 
graph = lst = [matrix_lin[i:i+n] for i in range(0, len(matrix_lin), n)]

det = recount_of_great_trees.recount(graph, n)


print (json.dumps(det))