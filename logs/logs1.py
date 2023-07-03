import sys
import re

array = []

with open("dhcpdsmall.log","r") as file:
    for line in file:
        m = re.search("((?:\w{2}:){5}\w{2})\s+\((iPhone|Alans-iPhone)\)",line,re.DOTALL)
        if m:
            array.append(m.group(1))
    #print(array)

single=set(array)
print(single)