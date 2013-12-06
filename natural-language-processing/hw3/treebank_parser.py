#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
import os
import fnmatch
import re
import gzip


if len(sys.argv) != 2:
    msg = "Usage: {} dataset"
    print >> sys.stderr, msg.format(sys.argv[0])
    exit(-1)

dataset = sys.argv[1]
PATTERN = "*.mrg"

def find_files(topdir, pattern):
    print >> sys.stderr, topdir, pattern
    for path, dirname, filelist in os.walk(topdir):
        for name in filelist:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(path,name)

def _format_parse(sentence):
    ordered_sent = []
    for line in sentence:
        for e in line:
            e = e[1:-1] # removing '(' and ')'
            tag, word = e.split()
            ordered_sent.append((tag, word))
    return ordered_sent

def parse_mrg(files):
    whole = []
    for i, f in enumerate(files):
        sentence = []
        for line in open(f):
            if line.startswith("("):
                if len(sentence) != 0:
                    whole.append(_format_parse(sentence))
                    sentence = []
            else:
                match = re.findall("\([^()]* [^()]*\)", line)
                if len(match) != 0:
                    sentence.append(match)
        if len(sentence) != 0:
            whole.append(_format_parse(sentence))
    print >> sys.stderr, "{} sentences are processed (total)".format(len(whole))
    print >> sys.stderr, "{} files are processed (total)".format(i+1)
    return whole

def print_tags_words(sentences):
    for sentence in sentences:
        print "<s>"
        for tag, word in sentence:
            print "{}\t{}".format(word, tag)
        print "</s>"

files = find_files(dataset, PATTERN)
print_tags_words(parse_mrg(files))
