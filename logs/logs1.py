import sys
import re

array = []

with open("dhcpdsmall.log","r") as file:
    for line in file:
        m = re.search("((?:\w{2}:){5}\w{2}).\(iPhone\)",line)
        if m:
            array.append(m.group(1))
    print(array)
