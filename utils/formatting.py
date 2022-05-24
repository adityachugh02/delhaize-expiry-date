import re

def formatting (x):
    
    pattern = re.compile('(?:\d+)[-/.](?:\d+)[-/.](?:20[22-55]|[22-55])')
    newlist = filter(pattern.match, x)

    return newlist