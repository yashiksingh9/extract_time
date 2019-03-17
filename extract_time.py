import nltk

def convert(t0):
    res = int("".join(map(str, t0)))
    return res

def convert(t1):
    res1 = int("".join(map(str, t1)))
    return res1

def hour(text):
    string = text
    istring = nltk.sent_tokenize(string)
    tstring = [nltk.word_tokenize(tstring) for tstring in istring]
    tagstring = [nltk.pos_tag(tstring) for tstring in tstring]
    length = len(tagstring[0])
    for i in range(0, length):
        if 'CD' in tagstring[0][i][1]:
            time = tagstring[0][i][0]
    htime = [nltk.word_tokenize(htime) for htime in time]
    t1 = htime[0]
    hour = convert(t1)
    return hour

def minute(text):
    string = text
    istring = nltk.sent_tokenize(string)
    tstring = [nltk.word_tokenize(tstring) for tstring in istring]
    tagstring = [nltk.pos_tag(tstring) for tstring in tstring]
    length = len(tagstring[0])
    for i in range(0, length):
        if 'CD' in tagstring[0][i][1]:
            time = tagstring[0][i][0]
    htime = [nltk.word_tokenize(htime) for htime in time]
    t0 = htime[2] + htime[3]
    minutes = convert(t0)

    return minutes



