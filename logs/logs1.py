import sys
import re

mac_address = set()

with open("dhcpdsmall.log","r") as file:
    for line in file:
        m = re.search("((?:\w{2}:){5}\w{2}).\(iPhone\)",line)
        if m:
            mac_address.append(m.group())
    print(mac_address)
