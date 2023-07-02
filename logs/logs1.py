import sys
import re

array = []

with open("dhcpdsmall.log","r") as file:
    for line in file:
        m = re.search(r"\b\s(\w{2}:){5}\w{2}\s.*\(iPhone\)",line)
        if m:
            array.append(m.group())
    print(array)
