#!/bin/env python3

import sys

def parse_points(file_name):
    fd = open(file_name).readlines()
    return [tuple(map(float, l.trim().split(' '))) for l in fd[1:]]

def find_centers(points):
    return 

def main(file_name):
    points = parse_points(file_name)
    possible_centers = find_centers(points)
    circles = calculate_radii(possible_centers)
    min_circle = min(circles, lambda x: x[1])
    print('{} {}\n{}'.format(min_circle[0][0], min_circle[0][1], min_circle[1]))

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Invalid number of arguments!', file=sys.stderr)
        print('Usage: python3 my_script.py input.txt', file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
