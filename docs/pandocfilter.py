#!/usr/bin/env python

"""
For now this filter is just a No-Op to see how  it works
"""
import sys
from pandocfilters import toJSONFilter, Link


def caps(key, value, format, meta):
    if key == "Cite":
        print >>  sys.stderr, "CITE", value
    if key == 'Link':
        print >> sys.stderr, "LINK", value
        return Link(*value)

if __name__ == "__main__":
    toJSONFilter(caps)
