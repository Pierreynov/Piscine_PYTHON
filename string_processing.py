import string 

def tokenize(sentence):
    sentence = sentence.lower()
    
    for i in sentence :
        if i in string.punctuation :
            sentence = sentence.replace(i, " ")
    sentence = sentence.split()
    return sentence
