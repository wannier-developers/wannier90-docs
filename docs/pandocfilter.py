#!/usr/bin/env python

"""
I try to make links work

Requirements -> that the section names are unique
What does not work yet: links to a file rather  that to its section header
"""
import sys
from pandocfilters import toJSONFilter, Link


def caps(key, value, format, meta):
#    print >> sys.stderr, key
#    if key == "Cite":
#        print >>  sys.stderr, "CITE", value
## example of value:
##  [[u'', [], []], [{u'c': u'here', u't': u'Str'}], [u'http://docs.mathjax.org/en/latest/tex.html#defining-tex-macros', u'']]
    if key == 'Link':
        dest = value[2][0]
        if '#' in dest and not  dest.startswith('http://') and not dest.startswith('https://') and not dest.startswith('/') and not dest.startswith('#'):
            value[2][0] = "#{}".format(dest.rpartition('#')[2])
            print >> sys.stderr, "[INFO] {} -> {}".format(dest, value[2][0])
            dest = value[2][0]
        if not  dest.startswith('http://') and not dest.startswith('https://') and not dest.startswith('#'):
            print >> sys.stderr, "[WARNING!] '{}' might not work".format(value[2][0])

        #print >> sys.stderr, "LINK", value
        return Link(*value)

if __name__ == "__main__":
    toJSONFilter(caps)
