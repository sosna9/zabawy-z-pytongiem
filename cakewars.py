

def order(sentence):
    result = []
    for index in range(1, len(sentence) + 1):
        for word in list(sentence.split()):
            if str(index) in word:
                result.append(word)
    return ' '.join(result)



key = lambda w:sorted(w)
print(key('dsffds'))

# def order(words):
#     return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


print(order('adf3jd fdklfd2js, afk1dfdsj tw4oja st5ara'))



