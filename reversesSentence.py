def reverseSentence(sentence):
    sSplit = sentence.split()
    sSplit.reverse()
    result = ""
    for word in sSplit:
        result = result+word+' '
    return result.rstrip()

reverseSentence("My name is Yuna")