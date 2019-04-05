#!/bin/python
import sys 
import math
import csv 

coords = []
coord1 = []
coord2 = []
output = []
vals = []

xyz_file = sys.argv[1]
 
f=open("dist.xyz","r")
total = f.readline()
for line in f:
        line = line.split()
        coords.append([line[1:4]])
#        print(coords[-1])
f.close()



Q1 = input('Would you like to calculate a bond distance? y or n \n')
while Q1 == 'y' or Q1 == 'Y':
        input_one = int(input("Enter the first atom number\n"))
        input_two = int(input("Enter the second atom number\n"))

        coord1 = coords[input_one]
        coord2 = coords[input_two]
#       coord1.append([input_one, input_two])
#       print([coord1])

        x1 = float(coord1[0][0])
        y1 = float(coord1[0][1])
        z1 = float(coord1[0][2])
        x2 = float(coord2[0][0])
        y2 = float(coord2[0][1])
        z2 = float(coord2[0][2])
        d = math.sqrt( (x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
        print(d)
        output = [str(input_one),str(input_two),str(d)]
        vals.append(output)

        Q1 = input('\nWould you like to calculate a bond distance? y or n \n')


myfile = open('bond_lengths.csv','w')
with myfile:
        writer = csv.writer(myfile)
        writer.writerows(vals)


print("He who controls the spice controls the universe")
sys.exit()
