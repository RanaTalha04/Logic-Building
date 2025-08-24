# Word Reversal in Sentence

def sentence_reverse(sentence):
    updated_sen = sentence.replace(" ","").lower()

    reversed_sen = updated_sen[::-1]

    if reversed_sen == updated_sen:
        return "Palindrome"
    else:
        return "Not Palindrome"

user_sen = input("Enter a sentence: ")
output_sen = sentence_reverse(user_sen)
print(output_sen)