import math
import os
import random
import re
import sys
from datetime import datetime, timedelta

def time_delta(t1,t2): # format of the input: Day dd mon year hh:mm:ss -xxxx (timezone)
    date_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, date_format)
    t2 = datetime.strptime(t2, date_format)
    return int(abs(t1 - t2).total_seconds())

if __name__ == '__main__' :
    n = int(input())

    for _ in range(n):
        t1 = input()
        t2 = input()

        print(time_delta(t1,t2))

# What I learned:
# 1. datetime library and datetime class
# 2. How to format a date
# 3. total_seconds function
# 4. date format types and directives