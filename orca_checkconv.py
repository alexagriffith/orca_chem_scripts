! /usr/bin/env python
import os
import time
import re

#workdir = os.environ["PBS_O_WORKDIR"]
#jobid =  os.environ["PBS_JOBID"]
#scratch = os.environ["SCR"]
# jobname = os.environ["JOB"]
jobname = "1263"
output_file = "/ccs/home/arnoldt/ag_files/nfe2s1.out"
#jobname + ".out"
sleeptime = 1
#end_flag = "               *****************************************************"
#begin_flag = "SCF ITERATIONS"
begin_re = re.compile("-{14}\nSCF ITERATIONS\n-{14}") #regexp to begin at the SCF iterations in the output file
iter_re = re.compile("(\d*)\s{2}(-?-\d*.\d*)\s{2}(-?-\d*.\d*)") #regexp in the iter
end_re = re.compile("\*{53}")                         #regexp to end at the end of the SCF iteration cycle
vals = []                        #empty list to store delta E vals
count = -1
energy_criteria = 2.0


def wait_time():
    time.sleep(sleeptime)

def main():
    check_good = True
    while check_good:
        data = openfile()
        check_good = criteria(data)
        wait_time()



def openfile():
    print("I am opening and reading file")
    f=open(output_file, "r")
    data = f.readlines()
    f.close()
    return data

def deltaE_criteria(data):
    global vals
    if len(vals) == 3:
        a = int(vals[0])
        b = int(vals[1])                         #delta E 1,2,3 -- a,b,c
        c = int(vals[2])
        if (a >= energy_criteria ) and (b >= energy_criteria ) and (c >= energy_criteria ):    #ADD ABSOLUTE VAL            # If delta E is more than or equal to 2 Hartrees for all 3 iter
            print('Job is not converging.')
            os.system("qdel jobname")     #change jobname 
        else:
            vals = []
    else:
        time.sleep(1)


def criteria(data):
    global count
    print("I am checking criteria")
    for line in data:
        m = iter_re.match(line)
        count += 1
        end = end_re.match(line)
        if m is not None:
            if len(m.groups()) < 2:
                continue
            else:
                vals.append(float(m.groups()[2]))

            deltaE_criteria(data)

        elif end:
            continue

#need2finish

if __name__ == "__main__":
    main()
