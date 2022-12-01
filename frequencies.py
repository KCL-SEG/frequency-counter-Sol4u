"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newlist = []
    for item in items:
        string = str(item)
        newlist.append(string)
    
    for item in newlist:
        if item in frequencies:
            frequencies[item] = frequencies[item]+1
        else:
            frequencies[item] = 1
    return frequencies
