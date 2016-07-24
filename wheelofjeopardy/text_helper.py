def pluralize(num, one, other):
    return one if num == 1 else other

def apostrophize(word):
    if word[-1] == 's':
        return "%s'" % word
    else:
        return "%s's" % word
