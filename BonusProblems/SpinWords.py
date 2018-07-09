# http://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    sentence_list=sentence.split(" ")
    new_sentence=''
    for word in sentence_list:
        if len(word) > 4:
            for letter in reversed(word):
                new_sentence +=letter
            new_sentence+=" "
        else:
            for letter in word:
                new_sentence+=letter
            new_sentence+=" "
    return new_sentence.strip()

print(spin_words('sroirraw wollef yeH'))