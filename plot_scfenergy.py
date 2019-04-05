#!/usr/bin/python
import re
import sys
import matplotlib.pyplot as plt

vals = []

find_exp = re.compile("(Coordinates)\sfrom\sORCA-job\s\w*\sE\s(-?-\d*.\d*)")
trj_file = sys.argv[1]



f=open(trj_file, "r")
data = f.readlines()
f.close()

for line in data:
    m = find_exp.match(line)
    if m:
        vals.append(float(m.groups()[1]))
        #print(vals)


#next step is to plot these values
plt.plot(vals)
plt.show()
