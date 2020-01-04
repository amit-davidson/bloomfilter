# pybloomfilter
Bloom filter implementation in python based on the MurmurHash3 hash function

## Overview


    >>> bl = BloomFilter(100000, 0.1)
    >>> bl.add('foo')
    >>> bl.add('bar')
    >>> bl.exist('foo')
    True
    >>> bl.exist('bar')
    True
    >>> bl.exist('baz')
    False