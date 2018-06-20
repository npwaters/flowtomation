#!/usr/bin/env python3

import sys


def main(save_name):
    lines = sys.stdin.read()
    lines = lines.split('\n')
    lines = [line for line in lines if len(line) > 0]

    output = open(save_name, 'a')
    for line in lines:
        output.write("{0}\n".format(line))

    output.close()


try:
    main(sys.argv[1])
except IndexError:
    sys.exit(1)

sys.exit(0)
