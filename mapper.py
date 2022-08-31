#!/usr/bin/env python
import sys

def read_stopwords(f):
    stopwords = []
    for line in f:
        line = line.strip().decode('utf-8')
        stopwords.append(line)
    return stopwords

def main():
    # get all lines from stdin
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # lowercase contents
        line = line.lower()

        # split the line into words; splits on any whitespace
        words = line.split()

        # stop_words
        stop_words = read_stopwords("english")

        # output tuples (word, 1) in tab-delimited format
        for word in words:
            if word not in stop_words:
                print '%s\t%s' % (word, "1")

if __name__ == "__main__":
    main()
