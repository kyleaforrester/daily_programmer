#!/usr/bin/env python3

import sys

def ducci_length(tup):
    past_tups = []
    steps = 0
    while (tup not in past_tups and len(list(filter(lambda x: x==0, tup))) != len(tup)):
        past_tups.append(tup)
        tup = [abs(tup[i]-tup[(i+1)%len(tup)]) for i in range(len(tup))]
        steps += 1
    return steps


if __name__=='__main__':
    lines = sys.stdin.readlines()
    lines = (tuple(map(lambda x: int(x.strip('() \r\t\n')),line.split(','))) for line in lines)
    for line in lines:
        print(ducci_length(line))
