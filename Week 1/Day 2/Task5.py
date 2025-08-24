# 🔹 Task 5: Word Reversal in Sentence

sen = "I Love Python as it is"
words = sen.split()
rev_sen = []
len_sen = len(words)
print(len_sen)

for char in range(len_sen - 1, -1, -1):
    rev_sen.append(words[char])

rev_sen_str = " ".join(rev_sen)
print(rev_sen_str)