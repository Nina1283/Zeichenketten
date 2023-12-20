import re

sentence = input("Enter a sentence: ")
sentence = re.sub("[,:;!?]", "", sentence)
print(sentence)
