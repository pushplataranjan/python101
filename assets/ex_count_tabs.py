#!/usr/bin/env python3
import os
import sys

def parse_file(path):
    """
    Parses the text file in the given path and returns space, tab & new line
    details.
    :arg path: Path of the text file to parse
    :return: A tuple with count of spacaes, tabs and lines. """
    fd = open(path)
    i=0
    spaces = 0
    tabs = 0
    for i,line in enumerate(fd):
            spaces += line.count(' ')
    tabs += line.count('\t') #Now close the open file fd.close()
        #Return the result as a tuple
    return spaces, tabs, i + 1

def main(path):
    """
    Function which prints counts of spaces, tabs and lines in a file.
    :arg path: Path of the text file to parse :return: True if the file exits or False. """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces %d. tabs %d. lines %d" % (spaces, tabs, lines))
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)