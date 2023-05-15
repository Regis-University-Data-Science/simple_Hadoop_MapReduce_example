#!/usr/bin/env python
import sys
import string

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lowercase
    line = line.lower()

    # https://stackoverflow.com/questions/34860982/replace-the-punctuation-with-whitespace
    # remove punctuation
    punctuations = list(string.punctuation) 
    for p in punctuations:
        if p in line:
            line = line.replace(p, '')

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and', 'is', 'a', 'this', 'that', 'it', 'to', 'in', 'an', 'as'])

    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
